# 1. 베이스 이미지 변경 (무거운 Dev Container 이미지 대신 표준 slim 이미지 사용)
FROM python:3.11-slim-bookworm

# 2. 필수 패키지 설치 및 최적화
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. 작업 디렉토리 설정 (Dev Container의 /workspace 대신 표준적인 /app 사용)
WORKDIR /app

# 4. 의존성 설치 (캐시 활용 최적화)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 복사
COPY . .

# 6. 실행 권한 부여 및 사용자 설정 (선택 사항이나 권장)
# CMD ["python", "main.py"]