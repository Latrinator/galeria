from django.urls import path, include

from . import views

urlpatterns = [
    #path("", views.logowanie, name="logowanie"),
    path("", include("django.contrib.auth.urls")),
    path("guest/", views.guest, name='guest'),
    path("bananas/", views.bananas, name='bananas'),
    path('employee/', views.employee, name='employee'),
    path('search/', views.search, name='search'),
    path("add/", views.add, name='add'),
    path("storage/", views.storage, name='storage'),

    path("api/artists/", views.api_artists, name='api_artists'),
    path('api/exhibits/', views.api_exhibits, name='api_exhibits'),
    path('api/storages/', views.api_storages, name='api_storages'),
    path('api/galleries/', views.api_galleries, name='api_galleries'),
    path('api/renters/', views.api_renters, name='api_renters'),
    path('api/rented/', views.api_rented, name='api_rented'),
    path('api/exhibitions/', views.api_exhibitions, name='api_exhibitions'),

    path('add_artist/', views.add_artist, name='add_artist'),
    path('add_renter/', views.add_renter, name='add_renter'),
    path('add_gallery/', views.add_gallery, name='add_gallery'),
    path('add_exhibit/', views.add_exhibit, name='add_exhibit'),

    path('add_storage/', views.add_storage, name='add_storage')
]

