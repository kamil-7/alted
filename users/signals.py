from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from users.models import Profile


@receiver(user_signed_up)
def create_profile(sender, **kwargs):
    Profile.objects.create(user=kwargs['user'])
