from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from users.serializers import UserSerializer


# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
