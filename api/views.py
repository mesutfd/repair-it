from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from car_repair_request.models import *
from .serializers import CarsSerializer


class CarsRepairApiList(ListCreateAPIView):
    queryset = CarRepairRequest.objects.all()
    serializer_class = CarsSerializer


