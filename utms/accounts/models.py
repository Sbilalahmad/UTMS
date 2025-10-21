from django.db import models
from django.contrib.auth.models import AbstractUser
ROLE_CHOICES = (
('admin', 'Administrator'),
('faculty', 'Faculty'),
('student', 'Student'),
)
class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
