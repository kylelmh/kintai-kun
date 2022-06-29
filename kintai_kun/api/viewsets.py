from kintai_kun.api.serializers import WorkTimestampSerializer
from rest_framework import viewsets
from rest_framework import permissions
from kintai_kun.api.serializers import *
from kintai_kun.models import *
from kintai_kun.api.helpers import *
import django_filters

class WorkTimestampViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAdminUser]
  serializer_class = WorkTimestampSerializer

  def get_queryset(self):
    queryset = WorkTimestamp.objects
    params = self.request.query_params
    month = parse_month(params)
    if 'name' in params:
      queryset = self.search_employee_obj_by_name(queryset, params['name'])
    return queryset.filter(created_on__month=month).order_by('-created_on')

class UserWorkTimestampViewSet(viewsets.ModelViewSet):
  serializer_class = WorkTimestampSerializer

  def get_queryset(self):
    params = self.request.query_params
    month = parse_month(params)
    return WorkTimestamp.objects.filter(created_on__month=month, employee__user=self.request.user)

class ShiftViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAdminUser]
  serializer_class = ShiftSerializer

  def get_queryset(self):
    params = self.request.query_params
    month = parse_month(params)
    queryset = Shift.objects.filter(date__month=month)
    if 'name' in params:
      queryset = search_employee_obj_by_name(queryset, params['name'])
    return queryset

class UserShiftViewSet(viewsets.ModelViewSet):
  serializer_class = ShiftSerializer

  def get_queryset(self):
    params = self.request.query_params
    month = parse_month(params)
    queryset = Shift.objects.filter(date__month=month, employee__user=self.request.user)
    return queryset

class EmployeeViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAdminUser]
  serializer_class = EmployeeSerializer
  queryset = Employee.objects.all()
  filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
 