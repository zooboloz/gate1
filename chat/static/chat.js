document.addEventListener("DOMContentLoaded", function () {
    const username = localStorage.getItem("username") || prompt("이름을 입력하세요:");
    localStorage.setItem("username", username);

    document.getElementById("username-display").innerText = `사용자: ${username}`;

    // 현재 프로토콜에 따라 WebSocket URL 결정 (http → ws, https → wss)
    const wsProtocol = window.location.protocol === "https:" ? "wss" : "ws";
    const wsUrl = `${wsProtocol}://${window.location.host}/ws/chat/`;

    // WebSocket 연결 생성
    const chatSocket = new WebSocket(wsUrl);

    // WebSocket 연결 이벤트 리스너
    chatSocket.onopen = function () {
        console.log("🔗 WebSocket 연결 성공:", wsUrl);
    };

    chatSocket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log("📩 받은 메시지:", data);

        const messageContainer = document.getElementById("chat-messages");
        const messageElement = document.createElement("div");

        if (data.type === "chat_message") {
            messageElement.innerHTML = `<strong>${data.username}:</strong> ${data.message}`;
            messageElement.classList.add("chat-message");
        } else if (data.type === "user_join") {
            messageElement.innerHTML = `<em>${data.username}님이 입장하셨습니다.</em>`;
            messageElement.classList.add("chat-notification");
        }

        messageContainer.appendChild(messageElement);
        messageContainer.scrollTop = messageContainer.scrollHeight; // 스크롤 자동 이동
    };

    chatSocket.onclose = function (event) {
        console.error("❌ WebSocket 연결이 닫혔습니다:", event);
    };

    chatSocket.onerror = function (error) {
        console.error("⚠️ WebSocket 오류 발생:", error);
    };

    // 메시지 전송 기능
    document.getElementById("chat-form").addEventListener("submit", function (event) {
        event.preventDefault();
        const messageInput = document.getElementById("chat-input");
        const message = messageInput.value.trim();

        if (message !== "") {
            chatSocket.send(JSON.stringify({
                type: "chat_message",
                username: username,
                message: message
            }));
            messageInput.value = ""; // 입력창 초기화
        }
    });
});

