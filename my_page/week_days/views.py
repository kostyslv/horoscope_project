from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
days_dict = {'monday': 'понедельник',
             'tuesday': 'вторник',
             'wednesday': 'среда',
             'thursday': 'четверг',
             'friday': 'пятница',
             'saturday': 'суббота',
             'sunday': 'воскресенье',
             }


def week_days_todo_list_by_number(request, todo_week: int):
    days_list = list(days_dict)
    if 0 > todo_week > len(days_list):
        return HttpResponseNotFound(f'Неверный номер дня недели - {todo_week}')
    day = days_list[todo_week - 1]
    redirect_url = reverse('week-day-name', args=[day])
    return HttpResponseRedirect(redirect_url)


def week_days_todo_list(request, todo_week: str):
    # description = days_dict.get(todo_week)
    # if description:
    #     return HttpResponse(description)
    # else:
    #     return HttpResponseNotFound
    return render(request, 'week_days/greeting.html')
