from django.urls import path
from .views import CarsRepairApiList
urlpatterns = [
    path('masoud', CarsRepairApiList.as_view(), name='cars-list-api-view')
]
