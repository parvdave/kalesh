from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Kalesh, Kaleshi
from django.core.mail import send_mail
from django.conf import settings
from . import outbound



@receiver(post_save, sender=Kalesh)
def post_create_kalesh(sender, instance, created, **kwargs):
    if created:
        # Create two Kaleshi objects for each email in the Kalesh
        Kaleshi.objects.create(kalesh=instance, 
                               kaleshi_slug=instance.kaleshi_slug_1, 
                               kaleshi_email=instance.email_1)
        Kaleshi.objects.create(kalesh=instance, 
                               kaleshi_slug=instance.kaleshi_slug_2, 
                               kaleshi_email=instance.email_2)
    if not created and instance.resolution:
        outbound.send_resolution_email(instance.resolution,instance.email_1,instance.email_2)
        print("sending resolution email")

@receiver(post_save, sender=Kaleshi)
def post_create_kaleshi(sender, instance, created, **kwargs):
    if created:
        outbound.send_email_for_kalesh(kaleshi_slug=instance.kaleshi_slug,kaleshi_email=instance.kaleshi_email)
    
    elif not created and instance.kaleshi_response:
        kalesh = instance.kalesh
        # Increase the response count
        kalesh.response_count += 1
        if kalesh.response_count == 2:
            resolution = outbound.resolve_kalesh(instance.kalesh)
            kalesh.resolution = resolution
        kalesh.save()
