from django.db import models
from django.urls import reverse
from star_ratings.models import Rating
from django.utils.translation import gettext_lazy as _


class StarTour(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    type = models.CharField(verbose_name=_("Type"), max_length=100)
    distance = models.CharField(verbose_name=_("Distance"), max_length=100)
    temp = models.CharField(verbose_name=_("Temp"), max_length=100)
    home_image = models.ImageField(
        verbose_name=_("Home image"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    image1 = models.ImageField(
        verbose_name=_("Image 1"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    image2 = models.ImageField(
        verbose_name=_("Image 2"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    image3 = models.ImageField(
        verbose_name=_("Image 3"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    about1 = models.CharField(verbose_name=_("About 1"), max_length=200)
    about2 = models.CharField(verbose_name=_("About 2"), max_length=200)
    about3 = models.CharField(verbose_name=_("About 3"), max_length=200)
    link = models.CharField(verbose_name=_("Link"), max_length=100, default="none")
    length = models.PositiveIntegerField(_("Length"))
    num_people = models.PositiveIntegerField(_("Number of people per tour"))

    def __str__(self):
        return self.name


class ConstellationTour(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    stars = models.CharField(verbose_name=_("Stars"), max_length=100)
    home_image = models.ImageField(
        verbose_name=_("Home image"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    image1 = models.ImageField(
        verbose_name=_("Image 1"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    image2 = models.ImageField(
        verbose_name=_("Image 2"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    image3 = models.ImageField(
        verbose_name=_("Image 3"),
        upload_to="static",
        default="static/stellar/constellations/BigDipper.jpg",
    )
    about1 = models.CharField(verbose_name=_("About 1"), max_length=200)
    about2 = models.CharField(verbose_name=_("About 2"), max_length=200)
    about3 = models.CharField(verbose_name=_("About 3"), max_length=200)
    link = models.CharField(verbose_name=_("Link"), max_length=100, default="none")
    length = models.PositiveIntegerField(_("Length"))
    num_people = models.PositiveIntegerField(_("Number of people per tour"))

    def __str__(self):
        return self.name
