from django.shortcuts import render

# APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

#  cookies
from django.http import HttpResponse
from django.shortcuts import redirect

# models
from apps.main.models import User, Plan

# serializers
from apps.main.serializers import UserRegisterSerializer

# register
from django.contrib import messages

# login
from django.contrib.auth import authenticate, login

# russian words
import re

# getobjects from database
from django.shortcuts import get_object_or_404

#  http
from django.http import JsonResponse

# csrf tokens
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def add_task(request, plan_id):
    """
    Представление для добавления задачи к плану.
    """
    plan = get_object_or_404(Plan, id=plan_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority', 'medium')

        # Проверяем, что все необходимые данные заполнены
        if not title:
            return JsonResponse({'error': 'Название задачи обязательно'}, status=400)

        # Создание задачи
        Task.objects.create(
            plan=plan,
            title=title,
            deadline=deadline,
            priority=priority
        )
        return redirect('planer')  # Перенаправление на главную страницу или куда нужно

    return render(request, 'add_task.html', {'plan': plan})

def check_user_visit(request):
    if not request.user.is_authenticated:  # Если пользователь не авторизован
        if not request.COOKIES.get('first_visit'):  # Проверяем cookie
            response = redirect('choseLorS')  # Перенаправляем на страницу приветствия
            response.set_cookie('first_visit', 'true', max_age=365*24*60*60)  # Устанавливаем cookie
            return response
        return redirect('login')  # Если не первый визит, но не авторизован, отправляем на логин
    else:  # Если пользователь авторизован
        return redirect('planer')  # Перенаправляем на страницу задач
    
def choseLorS(request):
    return render(request, 'choseLorS.html')

def signIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')

        # Проверка на существующего пользователя
        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким именем уже существует.")
            return render(request, 'signIn.html')

        # Проверка совпадения паролей
        if password != confirm_password:
            messages.error(request, "Пароли не совпадают.")
            return render(request, 'signIn.html')

        # Проверка длины пароля и отсутствия кириллицы
        if len(password) < 8 or re.search(r'[а-яА-Я]', password):
            messages.error(request, "Пароль должен быть не менее 8 символов и не содержать кириллицу.")
            return render(request, 'signIn.html')

        # Проверка возраста
        if age:
            try:
                age = int(age)
                if age < 13 or age > 148:
                    messages.error(request, "Возраст должен быть от 13 до 148 лет.")
                    return render(request, 'signIn.html')
            except ValueError:
                messages.error(request, "Возраст должен быть числом.")
                return render(request, 'signIn.html')

        # Создание пользователя
        messages.success(request, "Регистрация прошла успешно!")
    if request.method == "POST":
        form = UserRegisterSerializer(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('/planer/')  # Убедитесь, что этот URL существует
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegisterSerializer()

    return render(request, "signIn.html", {"form": form})

def logIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Передача объекта пользователя в функцию login
            login(request, user)
            messages.success(request, "Вы успешно вошли в аккаунт!")
            return redirect('/planer/')  # Переход на главную страницу (или другую)
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    return render(request, 'login.html')

def planer(request):
    plans = Plan.objects.all()  # Получаем все планы
    for plan in plans:
        if not plan.id:
            print(f"План без ID: {plan.title}")
    return render(request, 'planer.html', {'plans': plans})
