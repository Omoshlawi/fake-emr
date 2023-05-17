from django.shortcuts import render
from rest_framework import viewsets

from medication.models import AppointMent, HIVLabTest, ARTRegimen, PatientHivMedication
from medication.serializers import AppointMentSerializer, HIVLabTestSerializer, ARTRegimenSerializer, \
    PatientHivMedicationSerializer, PatientTriadSerializer
from users.models import Triad


# Create your views here.


class AppointMentViewSet(viewsets.ModelViewSet):
    queryset = AppointMent.objects.all()
    serializer_class = AppointMentSerializer
    filterset_fields = ['patient__patient_number', 'doctor']


class HIVLabTestViewSet(viewsets.ModelViewSet):
    queryset = HIVLabTest.objects.all()
    serializer_class = HIVLabTestSerializer
    filterset_fields = ['appointment__patient__patient_number']


class ARTRegimenViewSet(viewsets.ModelViewSet):
    queryset = ARTRegimen.objects.all()
    serializer_class = ARTRegimenSerializer


class PatientHivMedicationViewSet(viewsets.ModelViewSet):
    queryset = PatientHivMedication.objects.all()
    serializer_class = PatientHivMedicationSerializer
    filterset_fields = ['patient__patient_number']


class PatientsTriadsViewSet(viewsets.ModelViewSet):
    queryset = Triad.objects.all()
    serializer_class = PatientTriadSerializer
    filterset_fields = ['patient__patient_number']
