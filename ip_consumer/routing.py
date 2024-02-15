from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/ip_details/", consumers.IPAddressConsumer.as_asgi()),
]
