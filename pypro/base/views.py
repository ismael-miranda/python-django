# from django.http import HttpResponse
from pypro.modulos import facade
from django.shortcuts import render


def home(request):
    # retorna a mensagem
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
