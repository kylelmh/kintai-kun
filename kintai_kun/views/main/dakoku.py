from kintai_kun.views.custom_views import UserView
from django.http import HttpResponse
from kintai_kun.models import WorkTimestamp
from django.shortcuts import render
from django.utils import timezone
import json

class DakokuView(UserView):
  def get(self, request, *args, **kwargs):
    month = request.GET.get('month')
    if not month:
      month = timezone.now().month
    timestamps = WorkTimestamp.objects.filter(
      employee = request.user.employee,
      created_on__year = timezone.now().year,
      created_on__month = month
    ).order_by('-created_on')
    context = { 
      'timestamps': timestamps,
      'month': month,
    }
    return render(request, 'main/index.html', context=context)

  def post(self, request, *args, **kwargs):
    stamp_type = request.POST.get('stamp_type')
    new_stamp = WorkTimestamp(stamp_type=stamp_type, employee=request.user.employee)
    new_stamp.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')