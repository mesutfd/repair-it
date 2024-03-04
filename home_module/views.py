from django.http import HttpRequest
from django.shortcuts import render

from car_repair_request.models import CarRepairRequest
from utils.decorators import permission_checker_decorator_factory


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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
    with open("logs/logs.txt", 'a') as f:
        f.write(f"{get_client_ip(request)}\n")

    print(f"IPLogger: {get_client_ip(request)}")

    return render(request, 'home_module/index.html', context)
