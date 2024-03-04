from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from car_repair_request.models import *
from .serializers import CarsSerializer


class CustomCarsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CarsRepairApiList(ListCreateAPIView):
    queryset = CarRepairRequest.objects.filter(is_deleted=False)
    serializer_class = CarsSerializer
    pagination_class = CustomCarsPagination


class CarRepairDetailsApi(RetrieveAPIView):
    queryset = CarRepairRequest.objects.filter(is_deleted=False)
    serializer_class = CarsSerializer


class CarRepairRetrieveDeleteApi(RetrieveDestroyAPIView):
    queryset = CarRepairRequest.objects.filter(is_deleted=False)
    serializer_class = CarsSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarRepairDestroyApi(DestroyAPIView):
    queryset = CarRepairRequest.objects.filter(is_deleted=False)
    serializer_class = CarsSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # allowed_methods = ('GET', 'DELETE', 'HEAD', 'OPTIONS')
