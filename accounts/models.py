from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     print(instance, '🌹🌹🌹')
#     if created:
#         Profile.objects.create(
#             user=instance
#         )
