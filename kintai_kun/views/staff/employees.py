from django.shortcuts import render, redirect

from kintai_kun.views.custom_views import StaffView
from kintai_kun.models import Employee
from django.contrib.auth.models import User
from kintai_kun.forms import EmployeeForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone

class StaffEmployeesView(StaffView):
  def get(self, request):
    employees = Employee.objects.all().order_by('user__last_name')
    page_number = request.GET.get('page')
    context = {
      'employees' : Paginator(employees, 30).get_page(page_number)
    }
    return render(request, 'staff/employees/index.html', context=context)

class StaffEmployeeEditView(StaffView):
  def get(self, request, pk, *args, **kwargs):
    employee = Employee.objects.get(pk=pk)
    employee_form = EmployeeForm(initial = {
      'contract': employee.contract,
      'first_name':employee.user.first_name,
      'last_name':employee.user.last_name,
      'username': employee.user.username
    })
    context = {
      'employee': employee,
      'employee_form': employee_form
    }
    return render(request, 'staff/employees/edit.html', context=context)
  
  def post(self, request, pk, *args, **kwargs):
    employee = Employee.objects.get(pk=pk)
    user = employee.user
    employee_form = EmployeeForm(request.POST)
    if employee_form.is_valid():
      data = employee_form.cleaned_data
      user.first_name = data['first_name']
      user.last_name = data['last_name']
      user.username = data['username']
      if data['password']:
        user.set_password(data['password'])
      employee.contract = data['contract']
      user.save()
      employee.save()
      messages.success(request, f'{employee}が更新されました。')
      return redirect('staff_employees')
    else:
      messages.error(request, 'エラーが発生しました。')
      return self.get(request)

class StaffEmployeeCreateView(StaffView):
  def get(self, request):
    employee_form = EmployeeForm(request=request)
    context = {
      'employee_form': employee_form
    }
    return render(request, 'staff/employees/new.html', context=context)
  
  def post(self, request):
    employee_form = EmployeeForm(request.POST)
    if employee_form.is_valid():
      data = employee_form.cleaned_data
      pwd = data.pop('password')
      contract = data.pop('contract')
      user = User(**data)
      user.set_password(pwd)
      employee = Employee(user=user, contract=contract)
      user.save()
      employee.save()
      messages.success(request, f'従業員が追加されました。')
      return redirect('staff_employees')
    else:
      messages.error(request, 'エラーが発生しました。')
      return self.get(request)