from django.contrib import admin
from .models import PlanetaryTour
from django.utils.translation import gettext_lazy as _

class PlanetaryTourAdmin(admin.ModelAdmin):
    model = PlanetaryTour
    list_display = ('location_and_orbit', 'about_planet', 'name', 'length', 'num_people', 'image', 'image2', 'image3', 'image4')
admin.site.register(PlanetaryTour)