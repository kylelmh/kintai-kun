from kintai_kun.models import *
from rest_framework import serializers
from django.db import connections

class EmployeeSerializer(serializers.ModelSerializer):
  user = serializers.SlugRelatedField(
    read_only=True,
    slug_field='last_name'
  )
  class Meta:
    model = Employee
    fields = ['user', 'contract']

class WorkTimestampSerializer(serializers.ModelSerializer):
  employee = serializers.StringRelatedField()

  class Meta:
    model = WorkTimestamp
    fields = ['employee','created_on', 'memo', 'stamp_type']


class ShiftSerializer(serializers.ModelSerializer):
  employee = serializers.StringRelatedField()

  class Meta:
    model = Shift
    fields = ['employee', 'status', 'date', 'start_time', 'end_time', 'memo']
