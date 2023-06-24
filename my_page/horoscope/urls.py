from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type/', views.type),
    path('type/<str:element>/', views.elements, name='type-name'),
    path('<int:sign_zodiac>/', views.about_info_zodiac_signs_by_number),
    path('<str:sign_zodiac>/', views.about_info_zodiac_signs, name='horoscope-name'),
    ]