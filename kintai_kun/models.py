from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStampedModel(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    abstract = True

class Employee(TimeStampedModel):
  class ContractType(models.IntegerChoices):
    PARTTIME = 1
    CONTRACT = 2
    REGULAR = 3
  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  employee_id = models.CharField
  contract = models.IntegerField(choices=ContractType.choices)
  name = models.CharField
  photo = models.ImageField

class Shift(TimeStampedModel):
  employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
  start_time = models.DateTimeField
  end_time = models.DateTimeField

class WorkTimeStamp(TimeStampedModel):
  class StampType(models.IntegerChoices):
    WORK_START = 1
    WORK_END = 2
    BREAK_START = 3
    BREAK_END = 4
  stamp_type = models.IntegerField(choices=StampType.choices)
  employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    
    