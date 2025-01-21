# Register your models here.

from django.contrib import admin
from .models import Exhibit
from .models import Artist
from .models import Storage
from .models import Gallery
from .models import Renter
from .models import Rented
from .models import Exhibition



admin.site.register(Exhibit)
admin.site.register(Artist)
admin.site.register(Storage)
admin.site.register(Gallery)
admin.site.register(Renter)
admin.site.register(Exhibition)
admin.site.register(Rented)