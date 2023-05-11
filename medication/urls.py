from rest_framework import routers
from django.urls import path

from medication.views import AppointMentViewSet, HIVLabTestViewSet

router = routers.DefaultRouter()
router.register(prefix=r'appointments', viewset=AppointMentViewSet, basename='appointments')
router.register(prefix=r'test', viewset=HIVLabTestViewSet, basename='tests')

urlpatterns = router.urls
