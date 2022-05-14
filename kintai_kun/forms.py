from tracemalloc import start
from django import forms
from .models import *
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse

class ShiftForm(forms.ModelForm):
  class Meta:
    model = Shift
    # start_time = forms.DateTimeField(widget=forms.SelectDateWidget)
    fields = ['date', 'start_time', 'end_time', 'memo']
    widgets = {
      'date': forms.DateInput(attrs={'type': 'date'}),
      'start_time': forms.TimeInput(attrs={'type': 'time', 'min': '10:00'}),
      'end_time': forms.TimeInput(attrs={'type': 'time', 'max': '18:30', 'min': '14:00'}),
    }
  
  def clean(self):
    dt = super().clean()
    start_time = dt.get('start_time')
    end_time = dt.get('end_time')
    if start_time > end_time:
      raise ValidationError(
        "終業時間は始業時間より早い。"
      )

class StaffShiftForm(ShiftForm):
  class Meta(ShiftForm.Meta):
    fields = ['date', 'start_time', 'end_time', 'memo', 'status']

class EmployeeForm(forms.Form):
  def __init__(self, *args, request=None, **kwargs):
    super().__init__(*args, **kwargs)
    if request and request.path == reverse('staff_employee_create'):
      self.fields['password'].required = True

  contract = forms.ChoiceField(choices = [
    ('1','パート'),
    ('2', '契約・業務委託'),
    ('3', '正社員')
    ])
  last_name = forms.CharField(label='姓')
  first_name = forms.CharField(label='名')
  username = forms.CharField(label='ユーザー名', max_length=149)
  password = forms.CharField(label='パスワード', required=False, widget=forms.PasswordInput)
