from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from kintai_kun.views.custom_views import StaffView
from kintai_kun.models import WorkTimestamp, WorkTimestampChange
from kintai_kun.forms import StaffShiftForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.db import transaction

class StaffWTChangeView(StaffView):
  def get(self, request):
    context = {
      'wt_changes': WorkTimestampChange.objects.order_by('approving_employee', '-created_on')
    }
    return render(request, 'staff/worktimestamp_change/index.html', context=context)

  @transaction.atomic
  def post(self, request):
    pass