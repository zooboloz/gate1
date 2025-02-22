import os
from pathlib import Path
import dj_database_url

# 프로젝트의 기본 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# 보안 키 설정 (환경 변수에서 가져오기)
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-default-key")

# 디버그 모드 설정 (Railway 배포 시 False로 설정)
DEBUG = os.environ.get("DEBUG", "True") == "True"

# 허용된 호스트 설정 (Railway 도메인 포함)
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "gate1.onrender.com", os.environ.get("RAILWAY_URL", "")]

# 애플리케이션 정의
INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "chat",
]

# 미들웨어 설정
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ASGI 애플리케이션 설정 (WebSocket 지원)
ASGI_APPLICATION = "gate1.asgi.application"

# WSGI 애플리케이션 설정
WSGI_APPLICATION = "gate1.wsgi.application"

# 데이터베이스 설정 (환경 변수에서 `DATABASE_URL` 가져오기)
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# 인증 백엔드 설정
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 언어 및 시간대 설정
LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

# 정적 파일 설정
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "chat/static"]

# 채널 레이어 설정 (Redis 사용)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get("REDIS_URL", "redis://localhost:6379")],
        },
    },
}

# 기본 자동 필드 설정
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
