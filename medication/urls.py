from rest_framework import routers
from django.urls import path

from medication.views import AppointMentViewSet, HIVLabTestViewSet, ARTRegimenViewSet, PatientHivMedicationViewSet, \
    PatientsTriadsViewSet

router = routers.DefaultRouter()
router.register(prefix=r'appointments', viewset=AppointMentViewSet, basename='appointments')
router.register(prefix=r'regimens', viewset=ARTRegimenViewSet, basename='regimens')
router.register(prefix=r'patients-triads', viewset=PatientsTriadsViewSet, basename='patients-triads')
router.register(prefix=r'test', viewset=HIVLabTestViewSet, basename='tests')
router.register(prefix=r'', viewset=PatientHivMedicationViewSet, basename='hiv-prescription')

urlpatterns = router.urls
