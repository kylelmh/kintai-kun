from django import forms
from .models import Shift
from django.utils import timezone

class ShiftForm(forms.ModelForm):
  class Meta:
    model = Shift
    # start_time = forms.DateTimeField(widget=forms.SelectDateWidget)
    fields = ['start_time', 'end_time']
    widgets = {
      'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
      'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
    }


