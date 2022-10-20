from django.http import HttpRequest
from django.shortcuts import render
from utils.decorators import permission_checker_decorator_factory
from car_repair_request.models import CarRepairRequest

# Create your views here.
from django.views.generic import FormView


@permission_checker_decorator_factory()
def index(request: HttpRequest):
    current_user_id = request.user.id
    car_repairs = CarRepairRequest.objects.filter(user_id=current_user_id).all()
    repaired = CarRepairRequest.objects.filter(user_id=current_user_id, is_fixed=True).all()
    working = CarRepairRequest.objects.filter(user_id=current_user_id, is_fixed=False).all()
    print(request.user.username)
    context = {
        'repairs': car_repairs,
        'repaired': repaired,
        'working': working
    }
    return render(request, 'home_module/index.html', context)


