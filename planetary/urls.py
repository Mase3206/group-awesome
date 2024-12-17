from django.urls import path
from .views import PlanetaryListView, PlanetaryTourView

app_name = 'planetary'
urlpatterns = [
    path('', PlanetaryListView.as_view(), name="list"),
    path('planetary/tours/<int:pk>/', PlanetaryTourView.as_view(), name="tour_detail"),
]

    #path('', views.PlanetaryListView.as_view(), name="planetary_list"),
    #path('tour/<int:pk>/', views.PlanetaryTourView.as_view(), name='planetary_tour'),
    

    # path('mercury/', views.mercury_page, name="mercury_page"),
    # path('mars/', views.mars_page, name="mars_page"),
    # path('neptune/', views.neptune_page, name="neptune_page"),
    # path('pluto/', views.pluto_page, name="pluto_page"),
    # path('kepler/', views.kepler_page, name="kepler_page"),
    # path('sedna/', views.sedna_page, name="sedna_page"),
	# path('tour/<int:pk>/', views.PlanetaryTourView.as_view())
    # path('mercury/', views.mercury_page, name="mercury_page"),
    # path('mars/', views.mars_page, name="mars_page"),
    # path('neptune/', views.neptune_page, name="neptune_page"),
    # path('pluto/', views.pluto_page, name="pluto_page"),
    # path('kepler/', views.kepler_page, name="kepler_page"),
    # path('sedna/', views.sedna_page, name="sedna_page"),

