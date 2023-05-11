from django.shortcuts import render
from rest_framework import viewsets

from medication.models import AppointMent, HIVLabTest, ARTRegimen, PatientHivMedication
from medication.serializers import AppointMentSerializer, HIVLabTestSerializer, ARTRegimenSerializer, \
    PatientHivMedicationSerializer


# Create your views here.


class AppointMentViewSet(viewsets.ModelViewSet):
    queryset = AppointMent.objects.all()
    serializer_class = AppointMentSerializer


class HIVLabTestViewSet(viewsets.ModelViewSet):
    queryset = HIVLabTest.objects.all()
    serializer_class = HIVLabTestSerializer


class ARTRegimenViewSet(viewsets.ModelViewSet):
    queryset = ARTRegimen.objects.all()
    serializer_class = ARTRegimenSerializer


class PatientHivMedicationViewSet(viewsets.ModelViewSet):
    queryset = PatientHivMedication.objects.all()
    serializer_class = PatientHivMedicationSerializer
