from django.urls import path
from .views import chat_room, home

urlpatterns = [
    path("", home, name="home"),  # 홈 화면
    path("chat/", chat_room, name="chat_room"),  # 채팅방
]
