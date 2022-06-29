from kintai_kun.api.serializers import WorkTimestampSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from kintai_kun.api.serializers import *
from kintai_kun.models import *
from django.db.models import Q
from django.utils import timezone

class WorkTimestampViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAdminUser]
  serializer_class = WorkTimestampSerializer

  def get_queryset(self):
    queryset = WorkTimestamp.objects.all().prefetch_related('employee__user') 
    params = self.request.query_params
    month = timezone.now().month

    if 'month' in params:
      month = params['month']

    if 'name' in params:
      queryset = self.search_work_timestamp_by_name(queryset, params['name'])

    return queryset.filter(created_on__month=month).order_by('-created_on')

  def search_work_timestamp_by_name(self, wts, name):
    wts = wts.filter( Q(employee__user__first_name__icontains=name) |
                      Q(employee__user__last_name__icontains=name))
    return wts