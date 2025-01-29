from django.urls import path

from . import views

urlpatterns = [
    path("", views.logowanie, name="logowanie"),
    path("guest/", views.guest, name='guest'),
    path("bananas/", views.bananas, name='bananas'),
    path("api/artists/", views.api_artists, name='api_artists'),
    path("api/exhibits/", views.api_exhibits, name='api_exhibits'),
]

