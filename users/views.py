from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count, Min, Max, Avg, StdDev
from django.utils import timezone
from users.models import Patient, PatientNextOfKeen, Triad
from users.serializers import UserSerializer, PatientSerializer, PatientNextOfKeenSerializer, TriadSerializer


# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    search_fields = ("patient_number", "national_id", "phone_number")
    filterset_fields = ("patient_number", "national_id")


class PatientNextOfKeenViewSet(viewsets.ModelViewSet):
    serializer_class = PatientNextOfKeenSerializer
    queryset = PatientNextOfKeen.objects.all()


class TriadViewSet(viewsets.ModelViewSet):
    serializer_class = TriadSerializer
    queryset = Triad.objects.all()


class SummaryStatisticsViewSet(viewsets.ViewSet):
    def get_age(self, dob):
        print(dob)
        return 20

    def list(self, request):
        data = {
            'total_patients': Patient.objects.all().count(),
            'gender_distribution': {
                'male': Patient.objects.filter(gender='male').count(),
                'female': Patient.objects.filter(gender='female').count(),
            },
            # 'age_distribution': Patient.get_summary_statistics()
        }
        # print(Patient.get_summary_statistics())
        return Response(data=data)
