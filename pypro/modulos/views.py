from pypro.modulos import facade
from django.shortcuts import render


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhe.html', {"modulo": modulo})
