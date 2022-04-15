from django.urls import path

from . import views

urlpatterns = [
    path('', views.DakokuView.as_view(), name='dakoku'),
    path('shifts', views.ShiftsView.as_view(), name='dakoku_shifts'),
    path('staff', views.DakokuStaffView.as_view(), name='dakoku_staff'),
    path('employee_change_password', views.employee_change_password, name='employee_change_password')
]