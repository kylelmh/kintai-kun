from .custom_views import *
from .main.worktimestamp import *
from .main.shifts import *
from .apis.worktimestamp_change import *
from .staff.worktimestamp import *
from .staff.worktimestamp_change import *
from .staff.shifts import *
from .staff.employees import *

globals()['UserView'] = UserView
globals()['StaffView'] = StaffView
globals()['WTView'] = WTView
globals()['WTChangeAPI'] = WTChangeAPI
globals()['ShiftsView'] = ShiftsView
globals()['ShiftEditView'] = ShiftEditView
globals()['StaffWTView'] = StaffWTView
globals()['StaffShiftView'] = StaffShiftsView
globals()['StaffShiftEditView'] = StaffShiftEditView
globals()['StaffEmployeesView'] = StaffEmployeesView
globals()['StaffEmployeeEditView'] = StaffEmployeeEditView
globals()['StaffEmployeeCreateView'] = StaffEmployeeCreateView
globals()['ViewHelpers'] = ViewHelpers
globals()['StaffWTChangeView'] = StaffWTChangeView
