from rest_framework import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from users.models import Patient
from .models import HealthFacility, FacilityType, MaritalStatus, AppointMentType
from .serializers import HealthFacilitySerializer, FacilityTypeSerializer, MaritalStatusSerializer, \
    AppointMentTypeSerializer


# Create your views here.


class ApiRootView(APIView):
    def get(self, request):
        return Response({
            "users_url": reverse.reverse_lazy('users-list', request=request),
            "patients_url": reverse.reverse_lazy('patients-list', request=request),
            "marital_status": reverse.reverse_lazy('status-list', request=request),
            "appointment_types": reverse.reverse_lazy('appointment-types-list', request=request),
            "appointments": reverse.reverse_lazy('appointments-list', request=request),
            "hiv test": reverse.reverse_lazy('tests-list', request=request),
            "facilities_url": reverse.reverse_lazy('facilities-list', request=request),
            "facility types": reverse.reverse_lazy('types-list', request=request),
            "hiv regimens types": reverse.reverse_lazy('regimens-list', request=request),
            "patient hiv regimens prescription": reverse.reverse_lazy('hiv-prescription-list', request=request),
            "patients triads": reverse.reverse_lazy('patients-triads-list', request=request),
            "patients hiv tests": reverse.reverse_lazy('tests-list', request=request),
        })


class HIVClinicViewSet(viewsets.ModelViewSet):
    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilitySerializer


class HealthFacilityTypeViewSet(viewsets.ModelViewSet):
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer


class AppointMentTypeViewSet(viewsets.ModelViewSet):
    queryset = AppointMentType.objects.all()
    serializer_class = AppointMentTypeSerializer
