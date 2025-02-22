from django.urls import re_path
from .consumers import ChatConsumer  # 아래에서 만들 `ChatConsumer`를 임포트

websocket_urlpatterns = [
    re_path(r"ws/chat/$", ChatConsumer.as_asgi()),  # 웹소켓 경로
]
