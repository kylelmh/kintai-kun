from django.shortcuts import render, redirect

from kintai_kun.views.custom_views import StaffView
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone

class StaffEmployeesView(StaffView):
  def get(self, request):
    return render(request, 'staff/employees/index.html')
