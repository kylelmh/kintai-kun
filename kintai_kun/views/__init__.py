from .custom_views import *
from .main.dakoku import *
from .main.shifts import *
from .staff.dakoku import *
from .staff.shifts import *

globals()['UserView'] = UserView
globals()['StaffView'] = StaffView
globals()['DakokuView'] = DakokuView
globals()['ShiftsView'] = ShiftsView
globals()['ShiftEditView'] = ShiftEditView
globals()['StaffDakokuView'] = StaffDakokuView
globals()['StaffShiftView'] = StaffShiftsView
globals()['StaffShiftEditView'] = StaffShiftEditView
globals()['ViewHelpers'] = ViewHelpers
