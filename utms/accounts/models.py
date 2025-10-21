from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('admin', 'Administrator'),
    ('faculty', 'Faculty'),
    ('student', 'Student'),
)

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    # prevent clashes with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='accounts_user_set',  # <-- added
        related_query_name='accounts_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='accounts_user_set',  # <-- added
        related_query_name='accounts_user',
    )