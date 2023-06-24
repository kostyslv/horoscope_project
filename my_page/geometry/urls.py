from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='rectangle-area'),
    path('square/<int:width>/', views.get_square_area, name='square-area'),
    path('circle/<int:radius>/', views.get_circle_area, name='circle-area'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.func_get_rectangle_area),
    path('get_square_area/<int:width>/', views.func_get_square_area),
    path('get_circle_area/<int:radius>/', views.func_get_circle_area),
]
