from django.shortcuts import render

# APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

#  cookies
from django.http import HttpResponse
from django.shortcuts import redirect

# models
from apps.main.models import User

# serializers
from apps.main.serializers import UserRegisterSerializer

# register
from django.contrib import messages

# Create your views here.

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
        form = UserRegisterSerializer(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            # После регистрации, направляем на страницу todo
            return redirect('/planer/')  # Убедитесь, что здесь правильный путь
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegisterSerializer()

    return render(request, "signIn.html", {"form": form})

def login(request):
    return render(request, 'login.html')