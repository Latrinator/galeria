from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .models import Artist,Exhibit




def logowanie(request):
    template = loader.get_template('logowanie.html')
    return HttpResponse(template.render())

def guest(request):
    template = loader.get_template('guest.html')
    return HttpResponse(template.render())

def bananas(request):
    template = loader.get_template('bananas.html')
    return HttpResponse(template.render())

def employee(request):
    template = loader.get_template('employee.html')
    return HttpResponse(template.render())

def api_artists(request):
    artists = Artist.objects.all().values('name','surname','date_of_birth','date_of_death')
    return JsonResponse(list(artists), safe=False)

def api_exhibits(request):
    exhibits = Exhibit.objects.select_related('id_artist').all().values(
        'title','id_artist__name','id_artist__surname','type','height','width','weight'
        )
    return JsonResponse(list(exhibits), safe=False)