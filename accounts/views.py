from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


# Create your views here.
class UserUpdateView(LoginRequiredMixin, UpdateView):
	model = User
	login_url = settings.LOGIN_URL
	success_url = reverse_lazy('login')
	template_name = 'registration/update.html'

	fields = [
		'first_name',
		'last_name',
		'email',
	]

