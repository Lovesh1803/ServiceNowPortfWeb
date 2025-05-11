
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    # swap default username → email login if you like:
    email = models.EmailField('email address', unique=True)

    # any extra signup fields:
    phone = models.CharField('phone number', max_length=20, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username still required by AbstractUser


class PasswordResetToken(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token      = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used       = models.BooleanField(default=False)

    def is_valid(self):
        return (not self.used and
                timezone.now() - self.created_at < timedelta(hours=24))    