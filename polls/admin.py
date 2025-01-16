# Register your models here.

from django.contrib import admin
from .models import Exhibit
from .models import Artist



admin.site.register(Exhibit)
admin.site.register(Artist)