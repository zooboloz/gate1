from django.urls import path
from .views import chat_room  # chat_room 뷰 연결

urlpatterns = [
    path("", chat_room, name="chat_room"),  # `/chat/`에서 채팅 화면 보이도록 설정
]
