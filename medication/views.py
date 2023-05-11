from django.shortcuts import render
from rest_framework import viewsets

from medication.models import AppointMent, HIVLabTest
from medication.serializers import AppointMentSerializer, HIVLabTestSerializer


# Create your views here.


class AppointMentViewSet(viewsets.ModelViewSet):
    queryset = AppointMent.objects.all()
    serializer_class = AppointMentSerializer


class HIVLabTestViewSet(viewsets.ModelViewSet):
    queryset = HIVLabTest.objects.all()
    serializer_class = HIVLabTestSerializer
