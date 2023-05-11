from django.urls import path
from . import views
from rest_framework import routers

from .views import HIVClinicViewSet, HealthFacilityTypeViewSet, MaritalStatusViewSet, AppointMentTypeViewSet

router = routers.DefaultRouter()
router.register(viewset=HIVClinicViewSet, prefix='facilities', basename='facilities')
router.register(viewset=MaritalStatusViewSet, prefix='marital-status', basename='status')
router.register(viewset=AppointMentTypeViewSet, prefix='appointment-types', basename='appointment-types')
router.register(viewset=HealthFacilityTypeViewSet, prefix='types', basename='types')

urlpatterns = [
    path('', views.ApiRootView.as_view(), name='root'),
]
urlpatterns.extend(router.urls)
