from rest_framework import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from users.models import Patient
from .models import HealthFacility, FacilityType
from .serializers import HealthFacilitySerializer, FacilityTypeSerializer


# Create your views here.


class ApiRootView(APIView):
    def get(self, request):
        return Response({
            "users_url": reverse.reverse_lazy('users-list', request=request),
            "patients_url": reverse.reverse_lazy('patients-list', request=request),
            "facilities_url": reverse.reverse_lazy('facilities-list', request=request),
            "facility types": reverse.reverse_lazy('types-list', request=request),
        })


class HIVClinicViewSet(viewsets.ModelViewSet):
    queryset = HealthFacility.objects.all()
    serializer_class = HealthFacilitySerializer


class HealthFacilityTypeViewSet(viewsets.ModelViewSet):
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer
