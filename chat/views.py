from django.shortcuts import render

def home(request):
    return render(request, "chat/home.html")

def chat_room(request):
    username = request.GET.get("username", "")
    if not username:
        return render(request, "chat/home.html")  # 이름이 없으면 다시 홈으로 이동
    return render(request, "chat/chat_room.html", {"username": username})
