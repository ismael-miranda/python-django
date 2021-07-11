from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    # retorna a mensagem
    return HttpResponse('<html><body>Olá Mundo Django!</body></html>', content_type='text/html')
