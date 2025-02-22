document.addEventListener("DOMContentLoaded", function () {
    const chatLog = document.querySelector("#chat-log");
    const chatInput = document.querySelector("#chat-input");
    const sendButton = document.querySelector("#send-button");

    // 사용자 이름 가져오기
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get("username") || "익명";

    // WebSocket 연결 설정
    const chatSocket = new WebSocket(
        (window.location.protocol === "https:" ? "wss://" : "ws://") +
        window.location.host +
        "/ws/chat/"
    );

    // WebSocket 메시지 수신 이벤트
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const message = data.username + ": " + data.message;
        chatLog.value += message + "\n";
        chatLog.scrollTop = chatLog.scrollHeight; // 스크롤 자동 이동
    };

    // WebSocket 닫힘 이벤트
    chatSocket.onclose = function (e) {
        console.error("채팅 서버 연결이 종료되었습니다.");
    };

    // 메시지 전송 함수
    function sendMessage() {
        const message = chatInput.value.trim();
        if (message !== "") {
            chatSocket.send(JSON.stringify({
                "username": username,
                "message": message
            }));
            chatInput.value = "";
        }
    }

    // 전송 버튼 클릭 이벤트
    sendButton.addEventListener("click", function () {
        sendMessage();
    });

    // Enter 키 입력 시 메시지 전송
    chatInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });
});
