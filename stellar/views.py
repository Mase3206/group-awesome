from django.views.generic import TemplateView, DetailView, ListView
from .models import StarTour, ConstellationTour
from django.views import View
from django.urls import reverse_lazy, reverse

# Create your views here.
class StellarHomeView(ListView):
    template_name = "stellar.html"
    context_object_name = 'startours'
    model = StarTour

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'constellationtours': ConstellationTour.objects.order_by('pk')
        })
        return context

    def get_queryset(self):
        return StarTour.objects.order_by('pk')

class StarTourView(DetailView):
    model = StarTour
    template_name = 'star.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star tours"] = StarTour.objects.all()
        return context
    
class ConstellationTourView(DetailView):
    model = ConstellationTour
    template_name = 'constellation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["constellation tour"] = ConstellationTour.objects.all()
        return context
    
    