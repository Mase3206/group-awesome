from django.conf import settings
from django.contrib.auth.mixins import (
	AccessMixin, # control what happens if 403
	LoginRequiredMixin, # ensure user is logged in
    UserPassesTestMixin, # extra conditions that, if failed, throw a 403
)
from django.contrib.auth.models import User
from django.forms import BaseModelForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import SpaceTravelerProfileForm
from .models import SpaceTravelerProfile


class SpaceTravelerProfileCreateView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, CreateView):
	form_class = SpaceTravelerProfileForm
	login_url = settings.LOGIN_URL
	# redirect_field_name = 'index'
	success_url = reverse_lazy('home')
	template_name = 'profiles/create.html'


	def test_func(self, *args, **kwargs) -> bool:
		"""
		Ensure they *don't* already have a profile. If they do, they will be redirected.
		"""
		has_profile = None
		if self.request.user.is_authenticated:
			try:
				SpaceTravelerProfile.objects.get(real_account=self.request.user)
				has_profile = True
			except SpaceTravelerProfile.DoesNotExist:
				has_profile = False
		else:
			has_profile = False

		return not has_profile
		
		
	def handle_no_permission(self):
		"""
		When the currently signed-in user has a profile already, just redirect them to profiles:update instead.
		"""
		return redirect('profiles:update', pk=SpaceTravelerProfile.objects.get(real_account=self.request.user).pk)


	# the args here are kinda fucked, but it's worked so far, so it's probably fine
	def get_form(self, form_class: BaseModelForm | None = None) -> BaseModelForm:
		"""
		Set the real_account field (hidden) to link the profile to the actual user account that is currently signed in.
		"""
		form = super().get_form(form_class) #type:ignore
		form.initial['real_account'] = User.objects.get(pk=self.request.user.pk)
		return form


	def form_valid(self, form):
		"""
		Quadruple-check that the real_account field (hidden) is set to the currently signed-in user, then save the form.
		"""
		# get the pending object to be created
		obj: SpaceTravelerProfile = form.save(commit=False)
		# make sure this field is set to the current user
		obj.real_account = User.objects.get(pk=self.request.user.pk)
		# save and commit the object
		obj.save()
		# run the rest of the method from the parent class(es)
		return super().form_valid(form)


class SpaceTravelerProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, UpdateView):
	model = SpaceTravelerProfile
	form_class = SpaceTravelerProfileForm
	login_url = settings.LOGIN_URL

	success_url = reverse_lazy('home')
	template_name = 'profiles/update.html'

	permission_denied_message = "You cannot edit other user's profiles."

	# def handle_no_permission(self):
	# 	return redirect('home')

	def test_func(self, *args, **kwargs) -> bool:
		"""Function used by UserPassesTestMixin. Used to verify ownership of the profile to update is of the user."""
		# return super().test_func()
		thisModel = super().get_object(*args, **kwargs)
		return thisModel.real_account == self.request.user #type:ignore


class SpaceTravelerProfileViewView(DetailView):
	model = SpaceTravelerProfile
	template_name = 'profiles/view.html'



class SpaceTravelerProfilesListView(ListView):
	model = SpaceTravelerProfile
	template_name = 'profiles/all.html'