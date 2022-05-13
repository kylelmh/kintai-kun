from django.shortcuts import render, redirect

from kintai_kun.views.custom_views import StaffView
from kintai_kun.models import Employee
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
