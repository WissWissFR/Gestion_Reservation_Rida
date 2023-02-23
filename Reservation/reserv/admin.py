from django.contrib import admin
from .models import Ecole, Reservation, Evenement

# Register your models here.

admin.site.register(Ecole)
admin.site.register(Evenement)
admin.site.register(Reservation)

# admin.site.register(Ecole)