from django.urls import path, include
from .views import StellarHomeView, StarTourView, ConstellationTourView

urlpatterns = [
    path('stars/<int:pk>/', StarTourView.as_view(), name='star_tour'),
    path('constellations/<int:pk>/', ConstellationTourView.as_view(), name='constellation_tour'),
    path('', StellarHomeView.as_view(), name='stellar_home'),
]