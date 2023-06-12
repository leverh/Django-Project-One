from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)


    class Meta:
        db_table = 'user'

    # unique related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_permissions_custom'
    )

    # unique related_name for groups field
    groups = models.ManyToManyField(
        to='auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='user_groups_custom'
    )