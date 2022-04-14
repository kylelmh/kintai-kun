from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
  return render(request, 'main/index.html')

@login_required
def shifts(request):
  return render(request, 'shift_manager/index.html')

@login_required
def dakoku(request):
  if request.method == 'GET':
    return HttpResponseNotFound('ER')
  
  if request.method == 'POST':
    return HttpResponse(request, 'OK')