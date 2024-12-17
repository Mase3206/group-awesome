from django.test import TestCase
from django.urls import reverse
from .models import PlanetaryTour

# Create your tests here.
class PlanetaryTourModelTest(TestCase):

    def test_planetary_tour_creation(self):

        tour = PlanetaryTour.objects.create (
            name = "Mars Tour", 
            length = 10, 
            num_people = 45
        )

        self.assertEqual(tour.name, "Mars Tour")
        self.assertEqual(tour.length, 10)
        self.assertEqual(tour.num_people, 45)

    def test_planetary_tour_str_method(self):

        tour = PlanetaryTour.objects.create (
            name = "Mars Tour", 
            length = 10,
            num_people = 45
        )

        self.assertEqual(str(tour), "Mars Tour")