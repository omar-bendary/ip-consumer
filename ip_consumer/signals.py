from django.db.models.signals import post_save
from django.dispatch import receiver

from ip_consumer.tasks import update_ip_info

from .models import IPAddress


@receiver(post_save, sender=IPAddress)
def do_task_after_create(sender, instance, created, **kwargs):
    if created:
        print(f"IPAddress object {instance} has been created!")
        update_ip_info.delay(instance.ip_address)
