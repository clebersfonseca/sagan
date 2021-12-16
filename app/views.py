from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Olá mundo!')

def dashboardPanel(request):
    return HttpResponse('Painel de Indicadores')

def objectList(request):
    return HttpResponse('Lista de Objetos')

def tessObject(request, tessID):
    return HttpResponse('Objeto %s.' % tessID)
