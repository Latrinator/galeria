from django.db import models

# Create your models here.

class Exhibit(models.Model):
    id_exhibit = models.AutoField(primary_key=True)
    id_artist = models.ForeignKey('Artist', on_delete=models.CASCADE)  
    title = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    height = models.IntegerField()
    width = models.IntegerField()
    weight = models.IntegerField()
    status = models.CharField(max_length=20)
    is_valuable = models.BooleanField(default=False)

class Artist(models.Model):
    id_artist = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

class Storage(models.Model):
    id_storage_session = models.AutoField(primary_key=True)
    id_exhibit = models.ForeignKey('Exhibit', on_delete=models.CASCADE)
    cause = models.CharField(max_length=40)
    since = models.DateField()
    until = models.DateField(null=True, blank=True)

class Gallery(models.Model):
     id_gallery = models.AutoField(primary_key=True)
     name = models.CharField(max_length=30)
     localisation = models.CharField(max_length=30)

class Renter(models.Model):
     id_renter = models.AutoField(primary_key=True)
     name = models.CharField(max_length=30)
     localisation = models.CharField(max_length=30)

class Exhibition(models.Model):
    id_exhibition = models.AutoField(primary_key=True)
    id_exhibit = models.ForeignKey('Exhibit', on_delete=models.CASCADE)
    id_gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE)
    since = models.DateField()
    until = models.DateField(null=True, blank=True)

class Rented(models.Model):
    id_rented = models.AutoField(primary_key=True)
    id_exhibit = models.ForeignKey('Exhibit', on_delete=models.CASCADE)
    id_renter = models.ForeignKey('Renter', on_delete=models.CASCADE)
    since = models.DateField()
    until = models.DateField(null=True, blank=True)