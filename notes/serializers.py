from rest_framework import serializers

from .models import Note


# Сериализатор для модели Note, который преобразует объекты заметок в формат JSON и обратно
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
