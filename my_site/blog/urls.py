from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_post>/', views.all_posts_info_by_number),
    path('<str:name_post>/', views.all_posts_info),
    path('', views.posts),
]