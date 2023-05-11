from django.shortcuts import render
from rest_framework import viewsets

from medication.models import AppointMent
from medication.serializers import AppointMentSerializer


# Create your views here.


class AppointMentViewSet(viewsets.ModelViewSet):
    queryset = AppointMent.objects.all()
    serializer_class = AppointMentSerializer