from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/", include("chat.urls")),  # 채팅 앱 URL 연결
    path("ws/chat/", include("chat.routing")),  # WebSocket URL 추가
]
