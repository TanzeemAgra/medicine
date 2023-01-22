from django.shortcuts import render
from django.shortcuts import render
import joblib
#import prediction_service
import yaml
import os
import json
import pandas as pd
import numpy as np
from .models import medicine
import psycopg2

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    tanzeem=joblib.load('../saved_models/model.joblib')
    lis=[]
    lis.append(float(request.GET['age']))
    lis.append(float(request.GET['sex']))
    lis.append(float(request.GET['bmi']))
    lis.append(float(request.GET['children']))
    lis.append(float(request.GET['smoker']))
    lis.append(float(request.GET['region']))

    answer=tanzeem.predict([lis]).tolist()[0]

    b=medicine(age=request.GET['age'],sex=request.GET['sex'],bmi=request.GET['bmi'],
    children=request.GET['children'],smoker=request.GET['smoker'],region=request.GET['region'],
    charges=answer)
    b.save()

    return render(request, "index.html", {'answer':answer})