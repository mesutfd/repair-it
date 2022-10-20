from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from utils.decorators import permission_checker_decorator_factory
from .forms import *

# Create your views here.
from django.views.generic import FormView, CreateView, View, DetailView, TemplateView


class CarDeliverFormView(CreateView):
    template_name = 'car_repair_request/car_deliver_request.html'
    form_class = CarRepairModelForm
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super(CarDeliverFormView, self).get_context_data(**kwargs)
        return context


class CarDeliverView(View):
    def get(self, request):
        repair_form = CarRepairModelForm()
        context = {
            'repair_form': repair_form
        }

        return render(request, 'car_repair_request/car_deliver_request.html', context)

    def post(self, request: HttpRequest):
        repair_form = CarRepairModelForm(request.POST)
        user_id = request.user.id
        if repair_form.is_valid():
            car_type = repair_form.cleaned_data.get('car_type')
            car_number = repair_form.cleaned_data.get('car_number')
            short_description = repair_form.cleaned_data.get('short_description')
            current_user = User.objects.filter(id=user_id).first()

            new_car_repair_request = CarRepairRequest(
                user=current_user,
                car_type=car_type,
                car_number=car_number,
                short_description=short_description)
            new_car_repair_request.save()
            return redirect(reverse('login_page'))

        context = {
            'repair_form': repair_form,
        }
        return render(request, 'car_repair_request/car_deliver_request.html', context)


class CarRepairDetailView(TemplateView):
    template_name = 'car_repair_request/delivered-car.html'
    context_object_name = 'car_repairs'

    def get_context_data(self, **kwargs):
        context = super(CarRepairDetailView, self).get_context_data(**kwargs)
        cars = CarRepairRequest.objects.filter(id=kwargs['pk']).first()
        context['cars'] = cars
        return context


