from django.contrib import admin
from .models import SpaceTravelerProfile
from django.utils.translation import gettext_lazy as _


@admin.register(SpaceTravelerProfile)
class SpaceTravelerProfileAdmin(admin.ModelAdmin):
    list_display = ["real_account", "age", "home_planet", "language"]
