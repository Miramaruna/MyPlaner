from django.contrib import admin

#  models
from apps.main.models import User, Category, Task, Plan

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'age')
    list_filter = ('created_at', )
    search_fields = ('username', 'email')
    ordering = ('-created_at',)
    
admin.register(Category)

@admin.register(Plan)
class PanelAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'title')
    list_filter = ('user', 'category')
    search_fields = ('title', )
    ordering = ('-id',)
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('plan', 'title', 'priority', 'deadline', 'status', 'is_completed')
    list_filter = ('plan', 'priority', 'status')
    search_fields = ('title', )
    ordering = ('-id',)