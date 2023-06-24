import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from random import sample


posts_data = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Lorem ipsum dolor sit amet.'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
    },
]

def main(request):
    context = {'posts': random.sample(posts_data, 3)}
    return render(request, 'blog/index.html', context=context)


def posts(request):
    return render(request, 'blog/list_detail.html')


def all_posts_info(request, name_post: str):
    # if name_post == 'dog':
    #     return HttpResponse(f'Информация о посте dog')
    # elif name_post == 'charmander':
    #     return HttpResponse(f'Информация о посте charmander')
    # else:
    #     return HttpResponseNotFound('Неизвестный пост')
    post_name_dict = {'name_post': name_post}
    return render(request, 'blog/detail_by_name.html', context=post_name_dict)
    # return render(request, 'blog/list_detail.html')

def all_posts_info_by_number(request, number_post: int):
    number_data = {'number': number_post}
    # return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
    return render(request, 'blog/detail_by_number.html', context=number_data)

def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)

p = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]

people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]

def all_peoples(request):
    people_data = {
        'peoples': p
    }
    return render(request, 'blog/people.html', context=people_data)

def people_detail(request):
    people_data_detail = {
        'peoples_detail': people
    }
    return render(request, 'blog/people_detail.html', context=people_data_detail)