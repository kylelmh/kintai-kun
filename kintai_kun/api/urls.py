from django.urls import include, path
from kintai_kun.api.viewsets import WorkTimestampViewSet
from rest_framework import routers
from kintai_kun.api.viewsets import *

router = routers.DefaultRouter()
router.register(r'worktimestamps', WorkTimestampViewSet, 'worktimestamp')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]
