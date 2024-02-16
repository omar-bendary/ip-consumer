import json

from channels.generic.websocket import AsyncWebsocketConsumer


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
