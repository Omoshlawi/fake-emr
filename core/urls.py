from django.urls import path
from . import views
from rest_framework import routers

from .views import HIVClinicViewSet, HealthFacilityTypeViewSet

router = routers.DefaultRouter()
router.register(viewset=HIVClinicViewSet, prefix='facilities', basename='facilities')
router.register(viewset=HealthFacilityTypeViewSet, prefix='types', basename='types')

urlpatterns = [
    path('', views.ApiRootView.as_view(), name='root'),
]
urlpatterns.extend(router.urls)
