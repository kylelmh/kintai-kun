from django.urls import path, include
from kintai_kun.views import *

urlpatterns = [
    path('api/', include('kintai_kun.api.urls')),
    path('', DakokuView.as_view(), name='dakoku'),
    path('shifts', ShiftsView.as_view(), name='shifts'),
    path('shifts/<int:pk>/edit', ShiftEditView.as_view(), name='shift_edit'),
    path('staff', StaffDakokuView.as_view(), name='dakoku_staff'),
    path('staff/shifts', StaffShiftsView.as_view(), name='staff_shifts'),
    path('staff/shifts/<int:pk>/edit', StaffShiftEditView.as_view(), name='staff_shift_edit'),
    path('staff/employees', StaffEmployeesView.as_view(), name='staff_employees'),
    path('staff/employees/create', StaffEmployeeCreateView.as_view(), name='staff_employee_create'),
    path('staff/employees/<int:pk>/edit', StaffEmployeeEditView.as_view(), name='staff_employee_edit'),
    path('staff/employees/<int:pk>/delete', delete_employee, name='staff_employee_delete'),
    path('employee_change_password', ViewHelpers.employee_change_password, name='employee_change_password'),
    path('staff/csv', StaffCSVView.as_view(), name='staff_csv'),
]