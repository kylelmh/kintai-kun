from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from kintai_kun.views.custom_views import StaffView
from kintai_kun.models import Shift
from kintai_kun.forms import StaffShiftForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

class StaffShiftsView(StaffView):
  def get(self, request, *args, **kwargs):
    name = request.GET.get('name')
    month = request.GET.get('month')
    if not month:
      month = timezone.now().month
    shifts = Shift.objects.filter(
      date__year = timezone.now().year,
      date__month = month
      ).order_by('-date')
    if name:
      shifts = self.search_shift_by_name(shifts, name)
    page_number = request.GET.get('page')
    context = {
      'shifts' : Paginator(shifts, 50).get_page(page_number),
      'month': month
    }
    return render(request, 'staff/shifts/index.html', context=context)

  def post(self, request, *args, **kwargs):
    method = request.POST.get('method')
    status = request.POST.get('status')
    shift_pks = request.POST.getlist('shifts[]')
    shifts = Shift.objects.filter(pk__in = shift_pks)
    if method == 'patch':
      shifts.update(status=status)
    elif method == 'delete':
      shifts.delete()
    else:
      return HttpResponseNotAllowed()
    return redirect('staff_shifts')
  
  def search_shift_by_name(self, shifts, name):
    shifts = shifts.filter( Q(employee__user__first_name__icontains=name) |
                  Q(employee__user__last_name__icontains=name))
    return shifts

class StaffShiftEditView(StaffView):  
  def get(self, request, pk ,*args, **kwargs):
    shift = Shift.objects.get(pk=pk)
    shift_form = StaffShiftForm(instance=shift)
    context = {
      'shift_form': shift_form,
      'shift': shift,
    }
    return render(request, 'staff/shifts/edit.html', context=context)
  
  def post(self, request, pk, *args, **kwargs):
    shift = Shift.objects.get(pk=pk)
    shift_form = StaffShiftForm(request.POST, instance=shift)
    if shift_form.is_valid():
      shift = shift_form.save(commit=False)
      shift.save()
      messages.success(request, 'シフトが更新されました。')
      return redirect('staff_shifts')
    else:
      messages.error(request, 'シフト更新にエラーが発生しました。')
      return self.get(request)
