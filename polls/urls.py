from django.urls import path

from . import views

urlpatterns = [
    path("", views.logowanie, name="logowanie"),
    path("guest/", views.guest, name='guest'),
    path("bananas/", views.bananas, name='bananas'),
    path('employee/', views.employee, name='employee'),
    path('search/', views.search, name='search'),
    path("api/artists/", views.api_artists, name='api_artists'),
    path('api/exhibits/', views.api_exhibits, name='api_exhibits'),
    path('api/storages/', views.api_storages, name='api_storages'),
    path('api/galleries/', views.api_galleries, name='api_galleries'),
    path('api/renters/', views.api_renters, name='api_renters'),
    path('api/rented/', views.api_rented, name='api_rented'),
    path('api/exhibitions/', views.api_exhibitions, name='api_exhibitions')
]

