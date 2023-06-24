from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')
    return render(request, 'geometry/rectangle.html')

def get_square_area(request, width: int):
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * 2}')
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    # return HttpResponse(f'Площадь круга радусом {radius} равна {round(pi * (radius * 2), 1)}')
    return render(request, 'geometry/circle.html')


def func_get_rectangle_area(request, width: int, height: int):
    redirect_url = reverse('rectangle-area', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def func_get_square_area(request, width: int):
    redirect_url = reverse('square-area', args=(width, ))
    return HttpResponseRedirect(redirect_url)


def func_get_circle_area(request, radius: int):
    redirect_url = reverse('circle-area', args=[radius])
    return HttpResponseRedirect(redirect_url)
