from django.urls import path

from kintai_kun.views import *
from kintai_kun.views_old import employee_change_password

urlpatterns = [
    path('', DakokuView.as_view(), name='dakoku'),
    path('shifts', ShiftsView.as_view(), name='dakoku_shifts'),
    path('shifts/<int:pk>/edit', ShiftEditView.as_view(), name='dakoku_shift_edit'),
    path('staff', StaffDakokuView.as_view(), name='dakoku_staff'),
    path('staff/shifts', StaffShiftsView.as_view(), name='staff_shifts'),
    path('staff/shifts/<int:pk>/edit', StaffShiftEditView.as_view(), name='staff_shift_edit'),
    path('employee_change_password', ViewHelpers.employee_change_password, name='employee_change_password'),
]