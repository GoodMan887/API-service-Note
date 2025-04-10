from django.utils.timezone import localtime

from .models import Note

# Функция для проверки/обновления заметок, которые пришло время напомнить
def check_reminders():
    print('[check_reminders] Проверка напоминаний...')
    current_time = localtime()
    notes = Note.objects.filter(remind_at__lte=current_time, is_reminded=False)

    print(f'[check_reminders] Найдено {len(notes)} заметок для обновления')

    for note in notes:
        print(f"[Напоминание] {note.title} - {note.remind_at} | is_reminded: {note.is_reminded}")
        note.is_reminded = True
        note.save()
        print(f"[Обновлено] {note.title} - is_reminded: {note.is_reminded}")
