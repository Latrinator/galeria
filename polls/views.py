from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
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

@login_required
def employee(request):
    template = loader.get_template('employee.html')
    return HttpResponse(template.render())

@login_required
def search(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())

@login_required
def add(request):
    template = loader.get_template('add.html')
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

@login_required
@csrf_exempt
def add_artist(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST.get('date_of_death', None)
        if date_of_death == '':
            date_of_death = None
            Artist.objects.create(name=name, surname=surname, date_of_birth=date_of_birth, date_of_death=date_of_death)
        if date_of_death != '':
            if date_of_death < date_of_birth:       
                Artist.objects.create(name=name, surname=surname, date_of_birth=date_of_death, date_of_death=date_of_birth)
            else:
                Artist.objects.create(name=name, surname=surname, date_of_birth=date_of_birth, date_of_death=date_of_death)
        return redirect('employee')
    return render(request, 'add.html')

@login_required
@csrf_exempt
def add_renter(request):
    if request.method == 'POST':
        name = request.POST['name']
        localisation = request.POST['localisation']
        Renter.objects.create(name=name, localisation=localisation)
        return redirect('employee')
    return render(request, 'add.html')

@login_required
@csrf_exempt
def add_gallery(request):
    if request.method == 'POST':
        name = request.POST['name']
        localisation = request.POST['localisation']
        Gallery.objects.create(name=name, localisation=localisation)
        return redirect('employee')
    return render(request, 'add.html')

@login_required
@csrf_exempt
def add_exhibit(request):
    if request.method == 'POST':
        title = request.POST['title']
        id_artist = request.POST['id_artist']
        type = request.POST['type']
        height = request.POST['height']
        width = request.POST['width']
        weight = request.POST['weight']

        # Fetch the Artist instance
        try:
            artist = Artist.objects.get(id_artist=id_artist)
        except Artist.DoesNotExist:
            error_message = "The artist ID does not exist."
            return render(request, 'bananas.html', {'error_message': error_message})

        Exhibit.objects.create(title=title, id_artist=artist, type=type, height=height, width=width, weight=weight)
        return redirect('employee')
    return render(request, 'add.html')