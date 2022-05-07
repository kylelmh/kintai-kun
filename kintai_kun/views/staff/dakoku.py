from django.shortcuts import render
from kintai_kun.views.custom_views import StaffView
from kintai_kun.models import WorkTimestamp
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import HttpResponse
import csv

class StaffDakokuView(StaffView):
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)
  
  def get(self, request, *args, **kwargs):
    name = request.GET.get('name')
    month = request.GET.get('month')
    if not month:
      month = timezone.now().month
    timestamps = WorkTimestamp.objects.filter(
      created_on__year = timezone.now().year,
      created_on__month = month
    ).order_by('-created_on')
    if request.GET.get('name'):
      timestamps = self.search_work_timestamp_by_name(timestamps, name)
    timestamps = timestamps.order_by('-created_on')
    paginator = Paginator(timestamps, 40)
    page_number = request.GET.get('page')
    context = {
      'timestamps': paginator.get_page(page_number),
      'month': month
    }
    return render(request, 'staff/main/index.html', context=context)

  def search_work_timestamp_by_name(self, wts, name):
    wts = wts.filter( Q(employee__user__first_name__icontains=name) |
                      Q(employee__user__last_name__icontains=name))
    return wts

class StaffCSVView(StaffView):
  def get(self, request):
    month = request.GET.get('month')
    if not month:
      month = timezone.now().month
    response = HttpResponse(
      content_type="text/csv",
      headers={'Content-Disposition': f'attachment; filename="{month}.csv"'},
    )
    timestamps = WorkTimestamp.objects.filter(
      created_on__year = timezone.now().year,
      created_on__month = month
    ).order_by('employee', 'created_on')
    writer = csv.writer(response)
    for ts in timestamps:
      writer.writerow([ts.employee, ts.date, ts.local_time, ts.stamp_string])
    return(response)
