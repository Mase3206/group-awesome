from django.urls import path

from .views import (
	SpaceTravelerProfileCreateView,
	SpaceTravelerProfileUpdateView,
	SpaceTravelerProfileViewView,
	SpaceTravelerProfilesListView
)

app_name = 'profiles'
urlpatterns = [
	path('', SpaceTravelerProfilesListView.as_view(), name='all'),
	path('create/', SpaceTravelerProfileCreateView.as_view(), name='create'),
	path('<int:pk>/', SpaceTravelerProfileViewView.as_view(), name='view'),
	path('<int:pk>/update/', SpaceTravelerProfileUpdateView.as_view(), name='update'),
]
