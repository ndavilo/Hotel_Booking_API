from django.db import router
from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerView, ReservationView

router = DefaultRouter()
router.register('customer', CustomerView)
router.register('reservation', ReservationView)

urlpatterns = [
    path('', include(router.urls)),
]