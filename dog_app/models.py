from django.db import models


class Dog(models.Model):
    breed = models.CharField(max_length=100)  # Порода
    name = models.CharField(max_length=100)  # Кличка собаки
    owner = models.CharField(max_length=100)  # Хозяин при расширении и доработки я бы вынес в другю таблицу и ссылался на нее

    def __str__(self):
        return f"{self.name} ({self.breed})"
