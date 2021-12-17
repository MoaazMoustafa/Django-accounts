from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print(instance, '🌹🌹🌹')
    if created:
        Profile.objects.create(
            user=instance
        )
