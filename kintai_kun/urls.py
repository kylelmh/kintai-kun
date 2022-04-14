from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shifts', views.shifts, name='shifts'),
    path('dakoku', views.dakoku, name='dakoku')
]