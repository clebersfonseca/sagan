from ast import If
from django import http
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
import lightkurve as lk
from django.http import JsonResponse

def index(request):
    return render(request, 'app/home.html')

def dashboardPanel(request):
    return render(request, 'app/dashboard.html')

def about(request):
    return render(request, 'app/about.html')

def contribute(request):
    return render(request, 'app/contribute.html')

def objectList(request):
    df = pd.read_csv('exofop_tess_toisv1.csv', sep=';')
    jsonList = df.reset_index().to_json(orient='split')
    data = []
    data = json.loads(jsonList)
    context = {'d' : data}

    return render(request,'app/objectlist.html', context)

def returnModal(request):
    ticID = request.POST['id']
    idParam = 'TIC ' + ticID
    search_result = lk.search_lightcurve(idParam, mission='TESS')
    result = str(search_result)
    
    df = pd.read_json(result)

    return HttpResponse(df.to_json())

def tessObject(request, ticID, indexList):
    return render(request, 'app/object.html', ticID)