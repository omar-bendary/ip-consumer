from django.db import models

from ip_consumer.custom_model_fileds import IPAddressField


class IPAddress(models.Model):
    ip_address = IPAddressField()
    info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ip_address
