from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from kintai_kun.models import WorkTimestamp
from django.views import View
import json
# Create your views here.

class ShiftsView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

  def get(self, request, *args, **kwargs):
    return render(request, 'shift_manager/index.html')

class DakokuView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

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