from django.db import models
from django.contrib.auth.models import AbstractUser, User

LEVEL_CHOICES = (
    ('junior', 'Junior'),
    ('senior', 'Senior'),
    ('management', 'Management'),
)


class CustomUser(AbstractUser):
    initials = models.CharField(max_length=5, blank=False, default='N/A')
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES, default='junior')

    def __str__(self):
        return self.email






