from django.conf import settings
from django.conf.global_settings import LANGUAGES
from django.db import models
from django.utils.translation import gettext_lazy as _

PLANETS = [
    (0, "Mercury"),
    (1, "Venus"),
    (2, "Earth"),
    (3, "Mars"),
    (4, "Jupiter"),
    (5, "Saturn"),
    (6, "Uranus"),
    (7, "Neptune"),
    (8, "Pluto"),
]
SECURITY_QUESTIONS = (
    (0, "What was the name of your first pet?"),
    (1, "What street did you grow up on?"),
    (2, "What is your mother's maiden name?"),
    (3, "Where was your first date?"),
    (4, "What is the name of your best childhood friend?"),
)


class SpaceTravelerProfile(models.Model):
    REQUIRED_FIELDS = [
        "home_planet",
        "language",
        "security_question",
        "security_answer",
    ]
    home_planet = models.IntegerField(
        verbose_name=_("Planet"), choices=PLANETS, null=True, blank=False
    )
    age = models.PositiveIntegerField(verbose_name=_("Age"), null=True, blank=True)
    language = models.CharField(
        verbose_name=_("Language"),
        max_length=10,
        choices=LANGUAGES,
        null=True,
        blank=True,
    )
    bio = models.TextField(verbose_name=_("Bio"), max_length=200, null=True, blank=True)
    security_question = models.IntegerField(
        verbose_name=_("Security question"),
        choices=SECURITY_QUESTIONS,
        null=True,
        blank=False,
    )
    security_answer = models.CharField(
        verbose_name=_("Security answer"), max_length=30, null=True, blank=False
    )
    real_account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Real account"),
        on_delete=models.CASCADE,
        related_name="profile",
        null=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.real_account.username}'s profile"
