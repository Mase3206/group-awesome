from django.contrib import admin

from .models import SpaceTravelerProfile


# Register your models here.
@admin.register(SpaceTravelerProfile)
class SpaceTravelerProfileAdmin(admin.ModelAdmin):
	pass