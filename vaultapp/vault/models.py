from django.db import models
from django.contrib.auth.models import AbstractUser
import random

USER_COLOUR_CHOICES = [
    ('#326ba8', 'Blue'), ('#ba2f2f', 'Red'),
    ('#288a3d', 'Green'), ('#7f32a8', 'Purple'),
    ('#d99221', 'Orange')
]

def get_random_colour():
    return random.choice([colour[0] for colour in USER_COLOUR_CHOICES])

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff')
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    modules = models.JSONField(default=list)
    attendance = models.DecimalField(max_digits=5, decimal_places=1, default=100)
    grade = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    colour = models.CharField(max_length=10, choices=USER_COLOUR_CHOICES, default=get_random_colour())


class Module(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} - {self.code}"

