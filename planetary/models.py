from django.db import models
from django.utils.translation import gettext_lazy as _


class PlanetaryTour(models.Model):
    location_and_orbit = models.TextField(_("Location and orbit"))
    about_planet = models.TextField(_("About"))
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    length = models.PositiveIntegerField(_("Length"))
    num_people = models.PositiveIntegerField(_("Number of people per tour"))
    image = models.ImageField(
        verbose_name=_("Image"), upload_to="planetary_tours/", blank=True, null=True
    )
    image2 = models.ImageField(
        verbose_name=_("Image 2"), upload_to="planetary_tours/", blank=True, null=True
    )
    image3 = models.ImageField(
        verbose_name=_("Image 3"), upload_to="planetary_tours/", blank=True, null=True
    )
    image4 = models.ImageField(
        verbose_name=_("Image 4"), upload_to="planetary_tours/", blank=True, null=True
    )

    def __str__(self):
        return self.name
