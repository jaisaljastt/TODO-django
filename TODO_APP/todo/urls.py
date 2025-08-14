from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('api/tasks/', views.get_tasks, name='get-tasks'),
    path('api/tasks/create/', views.create_task, name='create-task'),
    path('api/tasks/<int:task_id>/update/', views.update_task, name='update-task'),
    path('api/tasks/<int:task_id>/delete/', views.delete_task, name='delete-task'),
]