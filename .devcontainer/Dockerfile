FROM mcr.microsoft.com/devcontainers/python:3.11

# PostgreSQL 15와 통신하기 위한 필수 클라이언트 툴 설치
RUN apt-get update && apt-get install -y postgresql-client

# 라이브러리 설치
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
    