from tracemalloc import start
from django import forms
from .models import Shift
from django.utils import timezone
from django.core.exceptions import ValidationError


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




