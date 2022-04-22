from django.urls import path

from . import views

urlpatterns = [
    path('', views.DakokuView.as_view(), name='dakoku'),
    path('shifts', views.ShiftsView.as_view(), name='dakoku_shifts'),
    path('shifts/<int:pk>/edit', views.ShiftEditView.as_view(), name='dakoku_shift_edit'),
    path('staff', views.DakokuStaffView.as_view(), name='dakoku_staff'),
    path('staff/shifts', views.StaffShiftsView.as_view(), name='staff_shifts'),
    path('employee_change_password', views.employee_change_password, name='employee_change_password'),
]