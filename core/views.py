from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView


# Create your views here.


class RootView(APIView):
    def get(self, request):
        return Response(data={
            'users': reverse_lazy("users-list", request=request)
        })