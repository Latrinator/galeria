from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def logowanie(request):
    template = loader.get_template('logowanie.html')
    return HttpResponse(template.render())