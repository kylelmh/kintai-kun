from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from kintai_kun.models import WorkTimestamp
from django.db.models import Q

from .forms import *

import json
# Create your views here.

class ShiftsView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

  def get(self, request, *args, **kwargs):
    shift_form = ShiftForm()
    context = {
      'shift_form': shift_form
    }
    return render(request, 'shifts/index.html', context=context)
  
  def post(self, request, *args, **kwargs):
    shift_form = ShiftForm(request.POST)
    if shift_form.is_valid():
      shift = shift_form.save(commit=False)
      shift.employee = request.user.employee
      shift.save()
      messages.success(request, 'シフトが作成されました。')
      return redirect('dakoku_shifts')
    else:
      messages.error(request, 'シフト作成にエラーが発生しました。')
      return render()

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

class DakokuStaffView(View):
  @method_decorator(staff_member_required)
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

def employee_change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)  # Important!
      messages.success(request, 'パスワード変更されました。')
      return redirect('employee_change_password')
    else:
      messages.error(request, 'エラーが発生しました。')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'main/password_change.html', {
    'form': form
  })