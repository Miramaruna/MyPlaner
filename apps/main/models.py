from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    age = models.IntegerField(
        verbose_name="Возраст пользователя",
        blank = True,
        null = True,
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название задачи"
    )
    description = models.TextField(
        verbose_name="Описание задачи",
        blank=True,
        null=True
    )
    priority = models.IntegerField(
        choices=[(1, 'Низкий'), (2, 'Средний'), (3, 'Высокий')],
        verbose_name="Приоритет задачи"
    )
    deadline = models.DateTimeField(
        verbose_name='Дедлайн'
    )
    status = models.IntegerField(
        choices=[(1, "В ожидании"), (2, "В работе"), (3, "Закончено")],
        verbose_name="Статус задачи"
    )
    is_completed = models.BooleanField(
        verbose_name="Выполнено ли"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"