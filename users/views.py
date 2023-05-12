from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

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
