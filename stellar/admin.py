from django.contrib import admin
from .models import StarTour, ConstellationTour

class StarTourAdmin(admin.ModelAdmin):
    model = StarTour
    list_display = (
        'name', 
        'type', 
        'distance', 
        'temp', 
        'home image',
        'image1', 
        'image2', 
        'image3', 
        'about1',
        'about2',
        'about3',
        'link',
        'length', 
        'num_people')
    
class ConstellationTourAdmin(admin.ModelAdmin):
    model = ConstellationTour
    list_display = (
        'name', 
        'stars', 
        'home image',
        'image1', 
        'image2', 
        'image3', 
        'about1',
        'about2',
        'about3',
        'link',
        'length', 
        'num_people')

admin.site.register(StarTour)
admin.site.register(ConstellationTour)