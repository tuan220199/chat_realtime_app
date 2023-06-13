from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='auth_users',  # Add a related name to the groups field in the auth app
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth_users',  # Add a related name to the user_permissions field in the auth app
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
