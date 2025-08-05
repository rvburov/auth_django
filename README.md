#### Авторизация и аутентификация
- **Способы регистрации и входа:**
    - Пароль и электронная почта
    - Через сервисы: Google, Yandex
- **Восстановление доступа:**
	- Отправка email с токеном для сброса пароля

#### Технологии
- **API**: Django REST Framework
- **ORM**: Django ORM
- **Контейнеризация**: Docker и Docker Compose
- **База данных**: PostgreSQL
- **База данных для тестирования**: SQLite 
- **CI/CD деплой**: GitHub Actions
- **Документирование API**: Swagger
- **Аутентификация/авторизация**: OAuth 2.0 (Google, GitHub, Yandex и др.) и JWT (JSON Web Tokens)
- **Продакшен-серверы**: Nginx/Gunicorn

#### Структура проекта
auth_django/                          # Корень проекта
├── backend/                          # Django-приложение
│   ├── auth_project/                 # Основной проект Django
│   │   ├── __init__.py
│   │   ├── settings/                 # Настройки Django (разделенные)
│   │   │   ├── __init__.py
│   │   │   ├── base.py               # Базовые настройки (без секретов)
│   │   │   ├── development.py        # DEBUG=True, SQLite
│   │   │   └── production.py         # DEBUG=False, PostgreSQL, HTTPS
│   │   ├── urls.py                   # Главные URL
│   │   └── wsgi.py
│   │
│   ├── authentication/               # Приложение аутентификации
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                 # ! Только модели для токенов/сессий
│   │   ├── serializers.py            # JWT/OAuth сериализаторы
│   │   ├── urls.py                   # auth/jwt/, auth/oauth/
│   │   ├── views.py                  # Логика JWT и OAuth
│   │   └── tests/
│   │       ├── __init__.py
│   │       ├── test_models.py
│   │       └── test_views.py         # ! Тесты разделены
│   │
│   ├── users/                        # Приложение пользователей
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                 # ! Кастомная модель User
│   │   ├── serializers.py            # Сериализаторы User
│   │   ├── urls.py                   # users/, users/me/
│   │   ├── views.py                  # CRUD для User
│   │   └── tests/
│   │       ├── __init__.py
│   │       ├── test_models.py
│   │       └── test_views.py
│   │
│   ├── manage.py
│   ├── requirements/                 # ! Разделенные зависимости
│   │   ├── base.txt                  # Django, drf, psycopg2
│   │   ├── dev.txt                   # pytest, debug-toolbar
│   │   └── prod.txt                  # gunicorn, whitenoise
│   │
│   ├── Dockerfile                    # Многоступенчатая сборка
│   └── .dockerignore                 # ! Игнорируемые файлы в Docker
│
├── nginx/
│   ├── nginx.conf                    # Конфиг для Django + статики
│   └── Dockerfile                    # Оптимизированный образ
│
├── .github/workflows/                # ! CI/CD
│   └── ci-cd.yml                     # Тесты + деплой
│
├── docker-compose.yml                # Dev и Prod конфигурации
├── docker-compose.prod.yml           # ! Отдельный для продакшена
├── .env.example                      # Шаблон переменных
├── .gitignore
└── README.md                         # Инструкции + диаграммы API

Важная информация:
Закройте лишние эндпоинты (например, /admin/ только для вашего IP).
