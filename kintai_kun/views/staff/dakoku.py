from django.shortcuts import render
from kintai_kun.views.custom_views import StaffView
from kintai_kun.models import WorkTimestamp
from django.db.models import Q
from django.core.paginator import Paginator

class StaffDakokuView(StaffView):
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)
  
  def get(self, request, *args, **kwargs):
    name = request.GET.get('name')
    timestamps = WorkTimestamp.objects.all()
    if request.GET.get('name'):
      timestamps = self.search_work_timestamp_by_name(timestamps, name)
    timestamps = timestamps.order_by('-created_on')
    paginator = Paginator(timestamps, 40)
    page_number = request.GET.get('page')
    context = {
      'timestamps': paginator.get_page(page_number)
    }
    return render(request, 'staff/main/index.html', context=context)

  def search_work_timestamp_by_name(self, wts, name):
    wts = wts.filter( Q(employee__user__first_name__icontains=name) |
                      Q(employee__user__last_name__icontains=name))
    return wts
