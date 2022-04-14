from django.urls import path

from . import views

urlpatterns = [
    path('dakoku', views.DakokuView.as_view()),
    path('shifts', views.ShiftsView.as_view())
]