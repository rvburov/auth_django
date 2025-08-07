# Базовый образ
FROM python:3.9-slim-buster as builder

# Установка зависимостей для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создание и активация виртуального окружения
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Финальный образ
FROM python:3.9-slim-buster

# Установка runtime зависимостей
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Копирование виртуального окружения из builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Рабочая директория
WORKDIR /app

# Копирование проекта
COPY . .

# Настройка переменных окружения
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings \
    PYTHONDONTWRITEBYTECODE=1

# Сборка статических файлов (для production)
RUN python manage.py collectstatic --noinput

# Порт для приложения
EXPOSE 8000

# Команда запуска (переопределяется в docker-compose)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "config.wsgi"]
