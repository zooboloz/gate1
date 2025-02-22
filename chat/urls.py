from django.urls import path
from .views import chat_room  # home 뷰 삭제

urlpatterns = [
    path("", chat_room, name="chat_room"),  # ✅ 빈 URL로 접속해도 채팅방으로 연결
    path("chat/", chat_room, name="chat_room"),  # 기존 URL도 유지
]
