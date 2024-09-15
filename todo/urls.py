from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),  # Added trailing slash for consistency

    path('my-login/', views.my_login, name="my-login"),  # Added trailing slash for consistency

    path('', views.home, name="home"),  # Added 'home' name for the root URL

    path('dashboard/', views.dashboard, name="dashboard"),  # Added trailing slash for consistency

    path('profile-manage/', views.profile_manage, name="profile-manage"),  # Added trailing slash for consistency

    path('create-task/', views.createTask, name="create-task"),  # Added trailing slash for consistency

    path('view-tasks/', views.viewTask, name="view-tasks"),  # Added trailing slash for consistency

    path('update-task/<str:pk>/', views.updateTask, name="update-task"),  # Added trailing slash for consistency

    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),  # Added trailing slash for consistency

    path('logout/', views.user_Logout, name="logout"),  # Added trailing slash for consistency
]
