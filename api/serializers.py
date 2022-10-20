from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from car_repair_request.models import *


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRepairRequest
        fields = '__all__'


class CarsSerializerDetail(serializers.ModelSerializer):
    class Meta:
        lookup_field = '__all__'
        serializer_class = CarRepairRequest
