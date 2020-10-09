from django.shortcuts import render
# from __future__ import print_function
from telesign.messaging import MessagingClient
from telesign.util import random_with_n_digits
import sys
from django.views.generic import ListView, CreateView, TemplateView
from .models import votante, candidato
from .forms import VotanteForm

# Create your views here.


def validar(request):
    return render(request, 'pages/validar.html')


def home(request):
    candidatos = candidato.objects.all()
    return render(request, 'pages/home.html', {'candidatos': candidatos})


def info(request):
    candidatos = candidato.objects.all()
    return render(request, 'pages/info.html', {'candidatos': candidatos})


def timeline(request):
    return render(request, 'pages/timeline.html')


def login(request):
    return render(request, 'pages/login.html')


class RegistrarVotante(CreateView):
    model = votante
    form_class = VotanteForm
    template_name = 'pages/login.html'


'''
if sys.version[0] == "3":
        raw_input = input
    customer_id = "37DED71D-078A-460C-B402-F02C3B50A3DC"
    api_key = "DPJ2DDdOO94UhGGRKMASAlkQdu/bAsi1xaQ09y6b0i65yfhqLkhSSBEJosVnzCwdZXmNZh5su8ZVFHIu9qJSZQ=="

    phone_number = "59176202571"
    verify_code = random_with_n_digits(5)

    message = "Tu código es: {}".format(verify_code)
    message_type = "OTP"

    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)

    user_entered_verify_code = raw_input(
        "Ingrese el código de verificación que se le envió: ")

    if verify_code == user_entered_verify_code.strip():
        return render(request, 'pages/home.html')
    else:
        return render(request, 'pages/errorLogin.html')
'''
