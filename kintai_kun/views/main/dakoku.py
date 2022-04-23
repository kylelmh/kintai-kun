from kintai_kun.views.custom_views import UserView
from django.http import HttpResponse
from kintai_kun.models import WorkTimestamp
from django.shortcuts import render
import json

class DakokuView(UserView):
  def get(self, request, *args, **kwargs):
    context = { 
      'timestamps': request.user.employee.worktimestamp_set.order_by('-created_on')[:40]
    }
    return render(request, 'main/index.html', context=context)

  def post(self, request, *args, **kwargs):
    stamp_type = request.POST.get('stamp_type')
    new_stamp = WorkTimestamp(stamp_type=stamp_type, employee=request.user.employee)
    new_stamp.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')