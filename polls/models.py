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

