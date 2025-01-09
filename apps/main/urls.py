from django.urls import path

# views
from apps.main.views import check_user_visit, choseLorS, signIn, logIn, planer, add_task

urlpatterns = [
    path('', check_user_visit, name="first"),
    path('choseLorS/', choseLorS, name="choseLorS"),
    path('login/', logIn, name="login"),
    # path('logout/', logout, name="logout"),
    path('signIn/', signIn, name="signIn"),
    path('planer/', planer, name="planer"),
    path('add_task/<int:plan_id>/', add_task, name='add_task')
]