from django.urls import path
from .views import UserUpdateView


urlpatterns = [
	path('<int:pk>/update/', UserUpdateView.as_view(), name='accounts_info_update'),
]
