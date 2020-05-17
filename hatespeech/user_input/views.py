from __future__ import unicode_literals
import json
from django.shortcuts import render, HttpResponse
from django.conf import settings
from . import reddit_hatespeech_userinput_processor as rhp
import sys
import pandas as pd

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        
        val = request.POST.get('url')
        return render(request,"user_input/index.html",{"output":rhp.url_process(val)[0]})

    return render(request,"user_input/index.html")

sys.stdout.flush()