import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from decouple import config


@shared_task
def send_ip_info_to_group(ip_info):
    """
    Send IP info to Channels group
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "ip_updates", {"type": "send_ip_update", "ip_info": ip_info}
    )


@shared_task
def fetch_ip_info(ip_address):
    api_token = config("API_TOKEN", cast=str)
    url = f"https://ipinfo.io/{ip_address}?token={api_token}"

    response = requests.get(url)
    ip_info = response.json()
    if response.status_code == 200:
        send_ip_info_to_group(ip_info)
    elif response.status_code == 404:
        error_message = ip_info.get("error", {}).get("message", "Unknown error")
        raise ValueError(f"IP:{ip_address} is wrong. {error_message}")
    else:
        raise ValueError(f"Unexpected error: {response.status_code}")

    return ip_info


@shared_task
def update_ip_info(ip_address):
    from ip_consumer.models import IPAddress

    ip_object = IPAddress.objects.get(ip_address=ip_address)
    existing_info = ip_object.info
    new_info = fetch_ip_info(ip_object.ip_address)
    if existing_info != new_info:
        ip_object.info = new_info
        ip_object.save()
