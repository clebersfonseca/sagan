from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.font_manager import json_dump, json_load
import pandas as pd
import json

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

def tessObject(request, tessID):
    return render(request, 'app/object.html', tessID)
