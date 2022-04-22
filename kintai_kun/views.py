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

from kintai_kun.models import *
from django.db.models import Q

from .forms import *
from datetime import datetime

import json
# Create your views here.

class ShiftsView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

  def get(self, request, *args, **kwargs):
    shift_form = ShiftForm()
    shifts = Shift.objects.filter(employee = request.user.employee).order_by('-updated_at')
    page_number = request.GET.get('page')
    context = {
      'shift_form': shift_form,
      'shifts' : Paginator(shifts, 10).get_page(page_number)
    }
    return render(request, 'shifts/index.html', context=context)
  
  def post(self, request, *args, **kwargs):
    shift_form = ShiftForm(request.POST)
    if shift_form.is_valid():
      shift = shift_form.save(commit=False)
      shift.employee = request.user.employee
      shift.status = 1
      shift.save()
      messages.success(request, 'シフトが作成されました。')
      return redirect('dakoku_shifts')
    else:
      messages.error(request, 'シフト作成にエラーが発生しました。')
      return self.get(request)

class ShiftEditView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)
  
  def get(self, request, pk ,*args, **kwargs):
    shift = Shift.objects.get(pk=pk)
    if not self.is_shift_editable(request, shift):
      return HttpResponseNotFound()
    shift_form = ShiftForm(instance=shift)
    context = {
      'shift_form': shift_form,
      'shifts': [shift],
    }
    return render(request, 'shifts/edit.html', context=context)
  
  def post(self, request, pk, *args, **kwargs):
    shift = Shift.objects.get(pk=pk)
    shift_form = ShiftForm(request.POST, instance=shift)
    if shift_form.is_valid() and self.is_shift_editable(request, shift):
      shift = shift_form.save(commit=False)
      shift.status = 1
      shift.save()
      messages.success(request, 'シフトが更新されました。')
      return redirect('dakoku_shifts')
    else:
      messages.error(request, 'シフト更新にエラーが発生しました。')
      return self.get(request)
  
  def is_shift_editable(self, request, shift):
    if shift.employee != request.user.employee:
      return False

    if shift.status != 1:
      return False

    return True

class StaffShiftsView(View):
  @method_decorator(staff_member_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

  def get(self, request, *args, **kwargs):
    name = request.GET.get('name')
    shifts = Shift.objects.all().order_by('-updated_at')
    if name:
      shifts = self.search_shift_by_name(shifts, name)
    page_number = request.GET.get('page')
    context = {
      'shifts' : Paginator(shifts, 50).get_page(page_number)
    }
    return render(request, 'staff/shifts/index.html', context=context)

  def post(self, request, *args, **kwargs):
    return HttpResponse(request.body)
  
  def search_shift_by_name(self, shifts, name):
    shifts = shifts.filter( Q(employee__user__first_name__icontains=name) |
                      Q(employee__user__last_name__icontains=name))
    return shifts

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