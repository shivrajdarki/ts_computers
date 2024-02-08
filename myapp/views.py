# myapp/views.py

from django.shortcuts import render, redirect
from .models import Service, SubService, Appointment
from .forms import AppointmentForm
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

def sub_service_form(request, service_id):
    service = Service.objects.get(pk=service_id)
    subservices = service.subservices.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            subservice_instance = form.cleaned_data['subservice']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Fetch the SubService instance using the selected option
            subservice = SubService.objects.get(pk=subservice_instance.id)

            appointment = Appointment.objects.create(
                service=service,
                subservice=subservice,
                name=name,
                phone=phone,
                date=date,
                time=time
            )

            return render(request, 'success_page.html', {'appointment': appointment})

    else:
        form = AppointmentForm()

    return render(request, 'sub_service_form.html', {'service': service, 'subservices': subservices, 'form': form})


def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_us_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})
