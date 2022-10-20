from django.urls import path
from .views import *

urlpatterns = [
    path('deliver-car-request/', CarDeliverView.as_view(), name='car-deliver-form-page'),
    path('delivered-car/<int:pk>', CarRepairDetailView.as_view(), name='delivered-car-page'),
]
