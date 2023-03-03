from django.db import models
from django.contrib.auth.models import User
from home_residents.models import HomeResident
# Create your models here.


class Device(models.Model):
    #device_id which distinguish it from other devices and it's unique for every device in the world
    device_id = models.TextField(null=False, blank=False)
    #Device model which is provided by the manufacturer
    device_model = models.TextField()
    brand = models.TextField()
    last_online = models.DateTimeField()
    owner = models.ForeignKey(HomeResident, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)