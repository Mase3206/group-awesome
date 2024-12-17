
import markdown2
from .models import PlanetaryTour
from django.views.generic import DetailView, ListView

# def planetary(request):
#     return render(request, 'planetary/planetary.html')

class PlanetaryListView(ListView):
    model = PlanetaryTour
    template_name = "planetary/all.html"
    context_object_name = 'planetary_tours'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print("Context:", context)  # This should print the context in your terminal
    #     return context

    # def get_queryset(self):
    #     return PlanetaryTour.objects.order_by('pk')
    

# class PlanetaryListView(ListView):
#     model = PlanetaryTour
#     template_name = 'planetary.html'  
#     context_object_name = 'planetary_tours'  

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print("Context:", context)
#         return context
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         print(queryset)
#         return queryset


class PlanetaryTourView(DetailView):
    template_name = 'planetary/tour.html'
    model = PlanetaryTour

    def get_object(self, queryset=None):
        # Get the PlanetaryTour object
        planetary_tour = super().get_object(queryset)

        # Convert the Markdown fields to HTML using markdown2
        planetary_tour.location_and_orbit_html = markdown2.markdown(planetary_tour.location_and_orbit)
        planetary_tour.about_planet_html = markdown2.markdown(planetary_tour.about_planet)

        return planetary_tour


# def mercury_page(request):
#     mercury_tour = get_object_or_404(PlanetaryTour, name="Mercury Tour")

#     return render(request, 'planetary/mercury_page.html', {'tour': mercury_tour, })

# def mars_page(request):
#     mars_tour = get_object_or_404(PlanetaryTour, name="Mars Tour")

#     return render(request, 'planetary/mars_page.html', {'tour': mars_tour})

# def neptune_page(request):
#     neptune_tour = get_object_or_404(PlanetaryTour, name="Neptune Tour")

#     return render(request, 'planetary/neptune_page.html', {'tour': neptune_tour})

# def pluto_page(request):
#     pluto_tour = get_object_or_404(PlanetaryTour, name="Pluto Tour")

#     return render(request, 'planetary/pluto_page.html', {'tour': pluto_tour})

# def kepler_page(request):
#     kepler_tour = get_object_or_404(PlanetaryTour, name="Kepler Tour")

#     return render(request, 'planetary/kepler_page.html', {'tour': kepler_tour})

# def sedna_page(request):
#     sedna_tour = get_object_or_404(PlanetaryTour, name="Sedna Tour")

#     return render(request, 'planetary/sedna_page.html', {'tour': sedna_tour})


