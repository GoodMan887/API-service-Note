# Note API

Минимальный API для управления заметками с напоминаниями, созданный на Django и Django REST Framework.

## Функции

- Создание, обновление, удаление и получение заметок.
- Напоминания на основе времени.

## Технологии

- Python 3.13.1
- Django 5.2
- Django REST Framework

## Установка

1. Клонировать репозиторий:
   
    git clone https://github.com/GoodMan887/API-service-Note.git
    
2. Установить зависимости:
   
    pip install -r requirements.txt
    
3. Применить миграции:
   
    python manage.py migrate
    
4. Запустить сервер:
   
    python manage.py runserver
    
## API

- GET /api/notes/ — Получить все заметки.
- GET /api/notes/{id}/ — Получить заметку по ID.
- POST /api/notes/ — Создать новую заметку.
- PUT /api/notes/{id}/ — Обновить заметку.
- DELETE /api/notes/{id}/ — Удалить заметку.
