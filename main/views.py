from django.shortcuts import render
import urllib, json

# Create your views here.
def home(request):
    url = 'https://api.covid19india.org/data.json'
    res = urllib.request.urlopen(url)
    data = json.loads(res.read())
    labels=[]
    chartdata=[]
  
    for state in data['statewise']:
        labels.append(state['state'])
        chartdata.append(state['confirmed'])
        
    return render(request,'home.html',{'data':data,'labels':labels,'chartdata':chartdata})
