from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TimeStampedModel(models.Model):
  created_on = models.DateTimeField(default=timezone.now)
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

class WorkTimestamp(TimeStampedModel):
  class StampType(models.IntegerChoices):
    WORK_START = 1
    WORK_END = 2
    BREAK_START = 3
    BREAK_END = 4
  stamp_type = models.IntegerField(choices=StampType.choices)
  employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
  memo = models.CharField(default='',max_length=255)
  date = models.DateField(default=timezone.now)
  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['employee', 'date', 'stamp_type'], name='unique_stamp_date')
    ]
  
  def __str__(self):
    return f'{self.employee}: {self.created_on.strftime("%Y-%m-%d %H:%M:%S")}, {self.stamp_string}'

  @property
  def stamp_string(self):
    stamps = ['出勤', '退勤', '休憩', '休憩終']
    return stamps[self.stamp_type-1]
    