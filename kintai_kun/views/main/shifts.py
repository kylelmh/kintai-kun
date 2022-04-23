from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from kintai_kun.views.custom_views import UserView
from kintai_kun.models import Shift
from kintai_kun.forms import ShiftForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone

class ShiftsView(UserView):
  def dispatch(self, request, *args, **kwargs):
    if request.user.employee.contract != 1:
      return HttpResponseNotAllowed()

    return super().dispatch(request, *args, **kwargs)

  def get(self, request, *args, **kwargs):
    shift_form = ShiftForm()
    month = request.GET.get('month')
    page_number = request.GET.get('page')
    if not month:
      month = timezone.now().month
    shifts = Shift.objects.filter(
      date__year = timezone.now().year,
      date__month = month,
      employee = request.user.employee
      ).order_by('-date')
    context = {
      'shift_form': shift_form,
      'shifts' : Paginator(shifts, 10).get_page(page_number),
      'month' : month
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
      return redirect('shifts')
    else:
      messages.error(request, 'シフト作成にエラーが発生しました。')
      return self.get(request)

class ShiftEditView(UserView):
  def dispatch(self, request, *args, **kwargs):
    if request.user.employee.contract != 1:
      return HttpResponseNotAllowed()

    return super().dispatch(request, *args, **kwargs)
  
  def get(self, request, pk ,*args, **kwargs):
    shift = Shift.objects.get(pk=pk)
    if not self.is_shift_editable(request, shift):
      return HttpResponseNotAllowed()
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
      return redirect('shifts')
    else:
      messages.error(request, 'シフト更新にエラーが発生しました。')
      return self.get(request)
  
  def is_shift_editable(self, request, shift):
    if shift.employee != request.user.employee:
      return False

    if shift.status != 1:
      return False

    return True
