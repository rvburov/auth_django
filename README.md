### Авторизация и аутентификация

1. **Способы регистрации и входа:**
    - Пароль и электронная почта
    - Через сервисы: Google, Yandex
2. **Восстановление доступа:**
    - Отправка email с токеном для сброса пароля

#### Технологии
- **API**: Django REST Framework и API Keys (Секретные ключи)
- **ORM**: Django ORM
- **Контейнеризация**: Docker и Docker Compose
- **База данных**: PostgreSQL
- **База данных для тестирования**: SQLite 
- **CI/CD деплой**: GitHub Actions
- **Документирование API**: Swagger/Redoc
- **Тестирование**: Pytest
- **Аутентификация/авторизация**: OAuth 2.0 (Google и Yandex) и JWT (JSON Web Tokens)
- **Продакшен-серверы**: Nginx/Gunicorn

#### Структура проекта
```
auth_django/                          # Корневая директория проекта
│
├── backend/                          # Backend-часть на Django
│   │
│   ├── config/                       # Основной конфигурационный модуль Django
│   │   ├── settings.py               # Настройки проекта
│   │   ├── urls.py                   # Корневая конфигурация URL
│   │   ├── asgi.py                   # ASGI-конфигурация
│   │   ├── wsgi.py                   # WSGI-конфигурация
│   │   └── logging.py                # Конфигурация логов
│   │
│   ├── authentication/               # Модули аутентификации (основная бизнес-логика)
│   │   │
│   │   ├── oauth/                    # Модуль OAuth аутентификации (google и yandex)
│   │   │   ├── oauth_config.py       # Конфигурации OAuth-провайдеров
│   │   │   ├── serializers.py        # Сериализаторы для OAuth
│   │   │   ├── urls.py               # Маршруты OAuth (/oauth/google/ и др.)
│   │   │   ├── views.py              # View-классы для OAuth
│   │   │   ├── models.py             # Модель для OAuth
│   │   │   ├── admin.py              # Админка для OAuth
│   │   │   ├── providers/            # Отдельные провайдеры
│   │   │   │   ├── google.py
│   │   │   │   └── yandex.py
│   │   │   └── tests/                # Тесты OAuth-функционала
│   │   │       ├── test_serializers.py
│   │   │       └── test_views.py
│   │   │
│   │   ├── jwt/                      # Модуль JWT аутентификации
│   │   │   ├── jwt_config.py         # Конфигурации JWT-токенов
│   │   │   ├── serializers.py        # Сериализаторы JWT-токенов
│   │   │   ├── urls.py               # Маршруты JWT (/jwt/create/ и др.)
│   │   │   ├── views.py              # View-классы для работы с токенами JWT
│   │   │   ├── admin.py              # ← опционально для BlacklistedToken
│   │   │   └── tests/                # Тесты JWT-функционала
│   │   │       ├── test_serializers.py
│   │   │       └── test_views.py
│   │   │
│   │   └── api_keys/                 # Модуль API-ключа для доступа разработчиков размещен в .env
│   │       └── views.py              # View-классы для API-ключа
│   │
│   ├── users/                        # Приложение работы с пользователями
│   │   ├── admin.py                  # Админка для пользователей
│   │   ├── models.py                 # Кастомная модель пользователя
│   │   ├── serializers.py            # Сериализаторы пользователей
│   │   ├── urls.py                   # URL для работы с пользователями
│   │   ├── views.py                  # View для операций с пользователями
│   │   └── tests/                    # Тесты пользовательского функционала
│   │       ├── test_serializers.py
│   │       └── test_views.py
│   │
│   ├── utils/                        # Общие утилиты
│   │   └── email.py                  # Отправка email если забыл пароль 
│   │   
│   ├── docs/                         # Документация API
│   │   ├── schemas.py                # Схемы для документации
│   │   └── docs_config.py            # Конфигурация Swagger/Redoc
│   │
│   ├── static/                       # Статические данные
│   │
│   ├── media/                        # Изображения
│   │
│   ├── requirements.txt              # Зависимости проекта
│   ├── manage.py                     # Утилита управления Django
│   ├── Dockerfile                    # Конфигурация Docker-образа
│   └── .dockerignore                 # Исключения для Docker-сборки
│
├── nginx/                            # Конфигурация Nginx
│   ├── nginx.conf                    # Основной конфиг Nginx
│   └── Dockerfile                    # Сборка Nginx-образа
│
├── .github/workflows/                # CI/CD автоматизация
│   └── ci-cd.yml                     # Конфигурация GitHub Actions
│
├── docker-compose.yml                # Конфигурация для разработки
├── docker-compose.prod.yml           # Конфигурация для продакшена
├── .env.example                      # Пример переменных окружения
├── .gitignore                        # Игнорируемые файлы Git
└── README.md                         # Основная документация проекта
```
Важная информация:
Закройте лишние эндпоинты (например, /admin/ только для вашего IP).

## Использование API

Добавьте ключ в заголовок запроса:
```bash
curl -X GET http://ваш-сервер/api/data/ \
  -H "X-API-KEY: your_secret_key_123"
```
