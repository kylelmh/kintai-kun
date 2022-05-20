from kintai_kun.views.custom_views import UserView
from django.http import HttpResponse
from kintai_kun.models import WorkTimestamp
from kintai_kun.forms import WTChangeForm
from django.shortcuts import render
from django.core.paginator import Paginator

from django.utils import timezone
import json

class WTChangeCreateView(UserView):
  def get(self, request, *args, **kwargs):
    context = {
      'wtc_form': WTChangeForm(),
      'timestamps': WorkTimestamp.objects.filter(employee=request.user.employee).order_by('-created_on')[:10],
      'disabled': True,
    }
    return render(request, 'main/worktimestamp_change/new.html', context=context)