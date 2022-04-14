from builtins import breakpoint
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.decorators import login_required
from kintai_kun.models import WorkTimestamp
import json
# Create your views here.

@login_required
def index(request):
  context = {
    'timestamps': request.user.employee.worktimestamp_set.order_by('-created_on')[:40]
  }
  return render(request, 'main/index.html', context=context)

@login_required
def shifts(request):
  return render(request, 'shift_manager/index.html')

@login_required
def dakoku(request):
  if request.method == 'GET':
    return HttpResponseNotFound('ER')
  
  if request.method == 'POST':
    stamp_type = request.POST.get('stamp_type')
    new_stamp = WorkTimestamp(stamp_type=stamp_type, employee=request.user.employee)
    new_stamp.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')