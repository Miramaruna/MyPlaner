from django.urls import path

# views
from apps.main.views import check_user_visit, choseLorS, signIn, login

urlpatterns = [
    path('', check_user_visit, name="first"),
    path('choseLorS/', choseLorS, name="choseLorS"),
    path('login/', login, name="login"),
    # path('logout/', logout, name="logout"),
    path('signIn/', signIn, name="signIn"),
    # path('planer/', planer, name="planer"),
]