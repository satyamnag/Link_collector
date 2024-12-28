from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.

def link_collector(request):
    if request.method=='POST':
        site=request.POST.get('site','')
        response=requests.get(site)
        soup=BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            links=link.get('href')
            link_text=link.string
            Link.objects.create(address=links, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data=Link.objects.all()

    return render(request, 'app_link_collector/result.html', {'data':data})

def delete(request):
    Link.objects.all().delete()
    return render(request, 'app_link_collector/result.html')