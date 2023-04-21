from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ A user profile model for maintaining delivery information and order history log """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=32, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=128, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=128, null=True, blank=True)
    default_country = CountryField(null=False, blank=True)
    default_postcode = models.CharField(max_length=16, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=32, null=True, blank=True)
    default_county = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update user profile """

    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
