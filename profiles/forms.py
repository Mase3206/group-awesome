from django.forms import ModelForm
from .models import SpaceTravelerProfile
from django.utils.translation import gettext_lazy as _


class SpaceTravelerProfileForm(ModelForm):
    class Meta:
        model = SpaceTravelerProfile
        fields = [
            "home_planet",
            "language",
            "age",
            "bio",
            "security_question",
            "security_answer",
            "real_account",
        ]
        exclude = ["real_account"]
