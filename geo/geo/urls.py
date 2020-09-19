from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from coordinates.viewsets import RequestHistoryViewSet

router = routers.DefaultRouter()
router.register('api/v1/history', RequestHistoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/coordinates', include("coordinates.urls")),
    path('', include(router.urls)),
]
