from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .models import Artist,Exhibit,Storage,Gallery,Renter,Exhibition,Rented




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

def search(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())

def api_artists(request):
    artists = Artist.objects.all().values('id_artist','name','surname','date_of_birth','date_of_death')
    return JsonResponse(list(artists), safe=False)

def api_exhibits(request):
    exhibits = Exhibit.objects.select_related('id_artist').all().values(
        'id_exhibit','id_artist','id_artist__name','id_artist__surname','title', 'type', 'height', 'width', 'weight','status','is_valuable'
    )
    return JsonResponse(list(exhibits), safe=False)

def api_storages(request):
    storages = Storage.objects.all().values('id_storage_session','id_exhibit', 'cause', 'since', 'until')
    return JsonResponse(list(storages), safe=False)

def api_galleries(request):
    galleries = Gallery.objects.all().values('id_gallery','name', 'localisation')
    return JsonResponse(list(galleries), safe=False)

def api_renters(request):
    renters = Renter.objects.all().values('id_renter','name', 'localisation')
    return JsonResponse(list(renters), safe=False)

def api_rented(request):
    renters = Rented.objects.all().values('id_rented','id_exhibit', 'id_renter', 'since', 'until')
    return JsonResponse(list(renters), safe=False)

def api_exhibitions(request):
    exhibitions = Exhibition.objects.all().values('id_exhibition','id_exhibit','id_gallery','since','until')
    return JsonResponse(list(exhibitions), safe=False)