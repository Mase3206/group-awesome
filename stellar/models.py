from django.db import models
from django.urls import reverse
from star_ratings.models import Rating

class StarTour(models.Model):
    name = models.CharField(max_length=100) #name of Star
    type = models.CharField(max_length=100) #Star Type
    distance = models.CharField(max_length=100) #Distance in light years from Earth
    temp = models.CharField(max_length=100) #Surface Temperature of Star

    home_image = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')

    image1 = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')
    image2 = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')
    image3 = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')

    about1 = models.CharField(max_length=200) #First  about bullet
    about2 = models.CharField(max_length=200) #Second about bullet
    about3 = models.CharField(max_length=200) #Third  about bullet

    link = models.CharField(max_length=100, default='none') #Link to NASA page

    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go

    def __str__(self):
        return self.name

class ConstellationTour(models.Model):
    name = models.CharField(max_length=100) #name of Star
    stars = models.CharField(max_length=100) #Notable stars within constellation

    home_image = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')

    image1 = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')
    image2 = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')
    image3 = models.ImageField(upload_to='static', default='static/stellar/constellations/BigDipper.jpg')

    about1 = models.CharField(max_length=200) #First  about bullet
    about2 = models.CharField(max_length=200) #Second about bullet
    about3 = models.CharField(max_length=200) #Third  about bullet

    link = models.CharField(max_length=100, default='none') #Link to NASA page

    length = models.PositiveIntegerField() #length in days
    num_people = models.PositiveIntegerField() #num of people who can go

    def __str__(self):
        return self.name