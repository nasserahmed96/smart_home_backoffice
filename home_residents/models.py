from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class HomeResident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)
