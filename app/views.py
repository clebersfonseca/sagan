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

def contribute(request):
    return render(request, 'app/contribute.html')

def objectList(request):
    df = pd.read_csv('exofop_tess_toisv1.csv', sep=';')
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
    df.rename(columns={"year" : "ano"})

    jsonData = df.reset_index().to_json(orient="records")
    data = []
    data = json.loads(jsonData)

    context = {'d' : data}

    return render(request, 'app/modal.html', context)

def returnModal(request):
    ticID = request.POST['id']
    idParam = 'TIC ' + ticID
    search_result = lk.search_lightcurve(idParam, mission='TESS')
    result = str(search_result)
    
    df = pd.read_json(result)

    return HttpResponse(df.to_json())

def tessObject(request, ticID, ind):
    
    context = {'ticID' : ticID, 'ind' : ind}

    return render(request, 'app/object.html', context)

def returnJson(request, ticID, ind):
    ticID = ticID
    obsIndex = ind

    idParam = 'TIC ' + str(ticID)
    search_result = lk.search_lightcurve(idParam, mission='TESS')

    lc = search_result[obsIndex].download()

    df = pd.DataFrame(lc.time.value, columns=["time"])
    df["data"] = lc.flux.value

    return JsonResponse(df.to_json(), safe=False)