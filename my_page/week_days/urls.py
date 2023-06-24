from django.urls import path
from . import views

urlpatterns = [
    path('<int:todo_week>/', views.week_days_todo_list_by_number),
    path('<str:todo_week>/', views.week_days_todo_list, name='week-day-name'),
]