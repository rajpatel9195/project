from django.db import models
from django.contrib.auth.models import User


# manuulay files
from .choiese import profation_choese, marrried_status_choese


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phonenumber = models.IntegerField()
    photo = models.ImageField(upload_to="profile/", null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    hobbies = models.CharField(max_length=100, null=True, blank=True)
    profation = models.CharField(
        max_length=100, choices=profation_choese, null=True, blank=True
    )
    marrid_status = models.CharField(
        max_length=100,
        choices=marrried_status_choese,
        null=True,
        blank=True,
    )
    cast = models.CharField(max_length=100, null=True, blank=True)
    subcast = models.CharField(max_length=100, null=True, blank=True)
