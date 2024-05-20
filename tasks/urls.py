from django.urls import path

from . import views

urlpatterns = [
    path('tasks', views.ListTask.as_view()),
    path('tasks/', views.CreateTask.as_view()),
    path('tasks/<int:id>', views.UpdateTask.as_view()),
    path('tasks/delete/<int:id>', views.DeleteTask.as_view()),
]