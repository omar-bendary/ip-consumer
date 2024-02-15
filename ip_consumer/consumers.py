import json

from channels.generic.websocket import AsyncWebsocketConsumer

# from ip_consumer.serializers import IPAddressSerializer

# from ip_consumer.tasks import get_ip_details

# class IPAddressConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         from time import sleep

#         text_data_json = json.loads(text_data)
#         ip_addresses = text_data_json.get("ip_addresses", [])
#         serializer = IPAddressSerializer(data=text_data_json)
#         serializer.is_valid(raise_exception=True)

#         for ip in ip_addresses:
#             try:
#                 ip_detail = get_ip_details(ip)

#                 await self.send(text_data=json.dumps({ip: ip_detail}))
#                 sleep(1)
#             except Exception as e:
#                 await self.send(text_data=json.dumps({"error": str(e)}))


# consumers.py


class IPAddressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "ip_updates"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def send_ip_update(self, event):
        ip_info = event["ip_info"]

        # Send IP info to WebSocket
        await self.send(text_data=json.dumps({"ip_info": ip_info}))
