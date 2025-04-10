from django.db import models


# Создание модели заметки
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    remind_at = models.DateTimeField()
    is_reminded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Метод для строкового представления объекта
    def __str__(self):
        return self.title
