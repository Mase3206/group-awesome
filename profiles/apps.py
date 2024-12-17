from django.apps import AppConfig
from django.apps import apps as django_apps


class ProfilesConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'profiles'



def get_all_profiles():
	return django_apps.get_model('profiles.SpaceTravelerProfile', require_ready=True)