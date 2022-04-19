from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TimeStampedModel(models.Model):
  created_on = models.DateTimeField(auto_now=timezone.now)
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
  contract = models.IntegerField(choices=ContractType.choices)

class Shift(TimeStampedModel):
  class StatusType(models.IntegerChoices):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    CHANGE_REQ = 4
  status = models.IntegerField(default=1, choices=StatusType.choices)
  employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
  start_time = models.DateTimeField(default=timezone.now)
  end_time = models.DateTimeField(default=timezone.now)

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
    