from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class RootView(APIView):
    def get(self, request):
        return Response(data={
            "hellow": 'wold'
        })