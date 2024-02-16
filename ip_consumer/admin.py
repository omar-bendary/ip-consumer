from django.contrib import admin

from ip_consumer.models import IPAddress


@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ["ip_address", "info", "created_at", "updated_at"]
