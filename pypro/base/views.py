from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    # retorna a mensagem
    return HttpResponse('Olá Mundo Django!')
