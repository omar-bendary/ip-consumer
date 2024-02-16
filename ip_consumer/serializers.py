import ipaddress

from rest_framework import serializers

from ip_consumer.models import IPAddress
from ip_consumer.tasks import update_ip_info


class IPAddressSerializer(serializers.Serializer):
    ip_addresses = serializers.ListField(child=serializers.CharField())

    def validate_ip_addresses(self, value):
        """
        Check if each IP address in the list is a valid IPv4 or IPv6 address.
        """
        for ip_address in value:
            try:
                ipaddress.ip_address(ip_address)
                ip_object, created = IPAddress.objects.get_or_create(
                    ip_address=ip_address
                )
                if not created:
                    update_ip_info.delay(ip_object.ip_address)

            except ValueError:
                raise serializers.ValidationError(
                    f"{ip_address} is not a valid IP address."
                )
        return value
