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
        invalid_ips = []
        for ip_address in value:
            try:
                ipaddress.ip_address(ip_address)
                ip_object, created = IPAddress.objects.get_or_create(
                    ip_address=ip_address
                )
                if not created:
                    update_ip_info.delay(ip_object.ip_address)
            except ValueError:
                invalid_ips.append(ip_address)

        if invalid_ips:
            raise serializers.ValidationError(
                f"The following IP address(es) are not valid: {', '.join(invalid_ips)}"
            )

        return value
