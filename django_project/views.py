#django_project/ view.py

from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'home.html')

class HomepageView(TemplateView):
    template_name = 'home.html'

class SignupView(TemplateView):
    template_name = 'signup.html'
