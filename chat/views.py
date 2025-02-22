from django.shortcuts import render

def chat_room(request):
    username = request.GET.get("username", "익명")  # ✅ URL에서 username 가져오기 (기본값: 익명)
    return render(request, "chat/chat_room.html", {"username": username})  # ✅ username 전달
