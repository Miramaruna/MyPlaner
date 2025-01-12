from django.urls import path

# views
from apps.main.views import check_user_visit, choseLorS, signIn, logIn, planer, add_task, create_plan, delete_plan, delete_task, complete_task

urlpatterns = [
    path('', check_user_visit, name="first"),
    path('choseLorS/', choseLorS, name="choseLorS"),
    path('login/', logIn, name="login"),
    # path('logout/', logout, name="logout"),
    path('signIn/', signIn, name="signIn"),
    path('planer/', planer, name="planer"),
    path('add_task/<int:plan_id>/', add_task, name='add_task'),
    path('create_plan/', create_plan, name="create_plan"),
    path('delete_plan/<int:plan_id>/', delete_plan, name="delete_plan"),
    path('delete_task/<int:task_id>/', delete_task, name="delete_task"),
    path('complete_task/<int:task_id>/', complete_task, name="complete_task"),
]