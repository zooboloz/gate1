import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "chat_room"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        print("✅ WebSocket 연결 성공:", self.channel_name)  # 로그 추가

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("⚠️ WebSocket 연결 종료:", self.channel_name)  # 로그 추가

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get("type", "message")

        if message_type == "enter":
            username = data["username"]
            message = f"{username}님이 입장하였습니다."
        else:
            username = data["username"]
            message = data["message"]

        print(f"📥 받은 메시지: {username} - {message}")  # 로그 추가

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "message_type": message_type
            }
        )

    async def chat_message(self, event):
        print(f"📤 브로드캐스트 메시지: {event}")  # 로그 추가
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
            "type": event["message_type"]
        }))
