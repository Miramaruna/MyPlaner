from django.shortcuts import render

#  cookies
from django.http import HttpResponse

# Create your views here.

def my_view(request):
    if not request.COOKIES.get('first_visit'):
        response = HttpResponse("Добро пожаловать на сайт впервые!")
        response.set_cookie('first_visit', 'true', max_age=365*24*60*60)  # Cookie на год
        return response
