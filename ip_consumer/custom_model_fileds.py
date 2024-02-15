import ipaddress

from django.core.exceptions import ValidationError
from django.db import models


class IPAddressField(models.CharField):
    description = "Field for storing IP addresses"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 15
        kwargs["unique"] = True
        super().__init__(*args, **kwargs)

    def validate_ip_address(self, value):
        try:
            ipaddress.ip_address(value)
        except ValueError:
            raise ValidationError("Invalid IP address format.")

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        self.validate_ip_address(value)
