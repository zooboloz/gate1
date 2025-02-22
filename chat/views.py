from django.shortcuts import render

def home(request):
    return render(request, "chat/home.html")  # ✅ 홈 화면

from django.shortcuts import render

def chat_room(request):
    username = request.GET.get("username", "Guest")  # ✅ 기본값을 "Guest"로 설정
    return render(request, "chat/chat_room.html", {"username": username})  # ✅ 바로 채팅방으로


    return render(request, "chat/chat_room.html", {"username": username})  # ✅ 채팅방 렌더링
