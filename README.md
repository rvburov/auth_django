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
- **Аутентификация/авторизация**: OAuth 2.0 (Google, GitHub, Yandex и др.) и JWT (JSON Web Tokens)
- **Продакшен-серверы**: Nginx/Gunicorn

#### Структура проекта
```
auth_django/                          # Корневая директория проекта
│
├── backend/                          # Backend-часть на Django
│   │
│   ├── auth_config/                  # Основной конфигурационный модуль Django
│   │   │
│   │   ├── settings/                 # Настройки проекта (разделены по средам)
│   │   │   ├── base.py               # Общие настройки для всех сред
│   │   │   ├── development.py        # Настройки для разработки (DEBUG=True)
│   │   │   └── production.py         # Продакшен-настройки (DEBUG=False)
│   │   │
│   │   ├── urls.py                   # Корневая конфигурация URL
│   │   └── wsgi.py                   # WSGI-конфигурация для развертывания
│   │
│   ├── authentication/               # Приложение аутентификации
│   │   │
│   │   ├── oauth/                    # Модуль OAuth аутентификации
│   │   │   ├── backends.py           # Кастомные бэкенды аутентификации
│   │   │   ├── providers.py          # Конфигурации OAuth-провайдеров
│   │   │   ├── serializers.py        # Сериализаторы для OAuth
│   │   │   ├── urls.py               # Маршруты OAuth (/oauth/google/ и др.)
│   │   │   ├── views.py              # View-классы для OAuth
│   │   │   └── tests/                # Тесты OAuth-функционала
│   │   │       ├── test_backends.py
│   │   │       └── test_views.py
│   │   │
│   │   ├── jwt/                      # Модуль JWT аутентификации
│   │   │   ├── serializers.py        # Сериализаторы JWT-токенов
│   │   │   ├── urls.py               # Маршруты JWT (/jwt/create/ и др.)
│   │   │   ├── views.py              # View-классы для JWT
│   │   │   └── tests/                # Тесты JWT-функционала
│   │   │       ├── test_serializers.py
│   │   │       └── test_views.py
│   │   │
│   │   ├── services/                 # Сервисный слой для бизнес-логики
│   │   │   ├── auth_services.py      # Сервисы аутентификации
│   │   │   └── token_services.py     # Сервисы работы с токенами
│   │   │
│   │   ├── middleware.py             # Проверка API-ключа для доступа разработчиков
│   │   ├── admin.py                  # Админ-панель для моделей
│   │   ├── apps.py                   # Конфигурация приложения
│   │   ├── models.py                 # Модели для токенов и сессий
│   │   ├── urls.py                   # Основные URL аутентификации
│   │   └── views.py                  # Общие view (выход из системы и др.)
│   │
│   ├── users/                        # Приложение работы с пользователями
│   │   ├── admin.py                  # Админка для пользователей
│   │   ├── apps.py                   # Конфигурация приложения
│   │   ├── models.py                 # Кастомная модель пользователя
│   │   ├── serializers.py            # Сериализаторы пользователей
│   │   ├── urls.py                   # URL для работы с пользователями
│   │   ├── views.py                  # View для операций с пользователями
│   │   └── tests/                    # Тесты пользовательского функционала
│   │       ├── test_models.py
│   │       └── test_views.py
│   │
│   ├── docs/                         # Документация API
│   │   ├── schemas.py                # Схемы для документации
│   │   └── docs_config.py            # Конфигурация Swagger/Redoc
│   │
│   ├── requirements/                 # Зависимости проекта
│   │   ├── base.txt                  # Основные зависимости
│   │   ├── dev.txt                   # Для разработки (тесты, отладка)
│   │   └── prod.txt                  # Для продакшена (оптимизации)
│   │
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
