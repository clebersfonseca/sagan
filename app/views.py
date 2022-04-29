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

def about(request):
    return render(request, 'app/about.html')

def objectList(request):
    df = pd.read_csv('exofop_tess_tois.csv', sep=';')
    jsonList = df.reset_index().to_json(orient='split')
    data = []
    data = json.loads(jsonList)
    context = {'d' : data}

    return render(request,'app/objectlist.html', context)

def modal(request):
    ticID = request.POST['id']
    idParam = 'TIC ' + ticID
    search_result = lk.search_lightcurve(idParam, mission='TESS')
    result = str(search_result)

    df = pd.read_json(result)

    jsonData = df.reset_index().to_json(orient="records")
    data = []
    data = json.loads(jsonData)

    context = {'d' : data}

    return render(request, 'app/modal.html', context)

def tessObject(request, ticID, ind):
    ticID = ticID
    obsIndex = ind

    idParam = 'TIC ' + str(ticID)
    search_result = lk.search_lightcurve(idParam, mission='TESS')
    
    lc = search_result[obsIndex].download()

    normalized_lc = lc.normalize()

    x = normalized_lc.time.value.tolist()
    y = [str(i) for i in normalized_lc.flux.value.tolist()]

    data = {'x' : x, 'y' : y, 'id' : ticID, 'index' : obsIndex}

    return render(request, 'app/object.html', data)

def foldLightCurve(request, ticID, ind):
    ticID = ticID
    obsIndex = int(ind)

    idParam = 'TIC ' + str(ticID)
    search_result = lk.search_lightcurve(idParam, mission='TESS')
    
    lc = search_result[obsIndex].download()

    normalized_lc = lc.normalize()

    pg = normalized_lc.to_periodogram(oversample_factor=10)

    folded_lc = normalized_lc.fold(period=4*pg.period_at_max_power)

    x = folded_lc.time.value.tolist()
    y = [str(i) for i in folded_lc.flux.value.tolist()]

    data = {'x' : x, 'y' : y, 'id' : ticID}

    return render(request, 'app/object.html', data)