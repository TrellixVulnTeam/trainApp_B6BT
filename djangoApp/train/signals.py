from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Stats

# This function creates a profile upon a user register
# When a user is saved a signal is sent and is received by the receiver create_profile func
# If user is created then create profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Profile)
def create_stats(sender, instance, created, **kwargs):
    if created:
        Stats.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def save_stats(sender, instance, **kwargs):
    instance.stats.save()

