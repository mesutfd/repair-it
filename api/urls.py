from django.urls import path
from .views import CarsRepairApiList, CarRepairDetailsApi, CarRepairRetrieveDeleteApi, CarRepairDestroyApi

urlpatterns = [
    path('masoud/', CarsRepairApiList.as_view(), name='cars-list-api-view'),
    path('masoud/<int:pk>/', CarRepairDetailsApi.as_view(), name='car-detail-api-view'),
    path('masoud/delete/<int:pk>/', CarRepairRetrieveDeleteApi.as_view(), name='car-delete-api-view'),
    path('masoud/destroy/<int:pk>/', CarRepairDestroyApi.as_view(), name='car-destroy-api-view'),
]
