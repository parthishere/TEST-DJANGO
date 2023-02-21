from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    phone_num = models.CharField(
        max_length=12, null=True, blank=True, default=None)
    birth_date = models.CharField(
        max_length=12, null=True, blank=True, default=None)

    def __str__(self):
        return self.user.name
