from django.urls import include, path
from kintai_kun.api.viewsets import WorkTimestampViewSet
from rest_framework import routers
from kintai_kun.api.viewsets import *

router = routers.DefaultRouter()
router.register(r'worktimestamps', WorkTimestampViewSet, 'worktimestamp')
router.register(r'user_worktimestamps', UserWorkTimestampViewSet, 'user_worktimestamp')
router.register(r'shifts', ShiftViewSet, 'shift')
router.register(r'user_shifts', UserShiftViewSet, 'user_shift')
router.register(r'employees', EmployeeViewSet, 'employee')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]
