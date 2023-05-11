from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from users.models import Patient
from users.serializers import UserSerializer, PatientSerializer


# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
