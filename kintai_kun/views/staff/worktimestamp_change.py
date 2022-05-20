from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from kintai_kun.views.custom_views import StaffView
from kintai_kun.models import WorkTimestamp
from kintai_kun.forms import StaffShiftForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.db import transaction

class StaffWTChangeView(StaffView):
  def get(self, request):
    return render(request, 'staff/worktimestamp_change/index.html')

  @transaction.atomic
  def post(self, request):
    pass