from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}


def index(request):
    zodiacs = list(zodiac_dict)
    # li_elements = ''
    # for sign in zodiac_list:
    #     redirect_path = reverse('horoscope-name', args=[sign])
    #     li_elements += f'<li> <a href="{redirect_path}">{sign.title()}</a></li>'
    # response = f"""
    # <ul>
    #     {li_elements}
    # </ul>
    # """
    context = {
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/index.html', context=context)


dict_zodiac_of_element = {'fire': ['aries', 'leo', 'sagittarius'],
                          'earth': ['taurus', 'virgo', 'capricorn'],
                          'air': ['gemini', 'libra', 'aquarius'],
                          'water': ['cancer', 'scorpio', 'pisces']}


def type(request):
    elem_list = list(dict_zodiac_of_element)
    li_types = ''
    for elem in elem_list:
        redirect_path = reverse('type-name', args=[elem])
        li_types += f'<li> <a href="{elem}">{elem.title()}</a></li>'
    response_t = f"""
        <ul>
            {li_types}
        </ul>
        """
    return HttpResponse(response_t)


def elements(request, element):
    type_list = dict_zodiac_of_element.get(element)
    li_signs = ''
    for sign in type_list:
        redirect_path_type = reverse('horoscope-name', args=[sign])
        li_signs += f'<li><a href="{redirect_path_type}">{sign.title()}</a></li>'
    response_type = f"""
        <ul>
            {li_signs}
        </ul>
        """
    return HttpResponse(response_type)
    # redirect_url = reverse('horoscope-name', args=[sign])
    # return HttpResponseRedirect(redirect_path_type)


def about_info_zodiac_signs(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac.title(),
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def about_info_zodiac_signs_by_number(request, sign_zodiac: int):
    # zodiac_list = list(zodiac_dict)
    # if sign_zodiac > len(zodiac_list) and sign_zodiac < 0:
    #     return HttpResponseNotFound(f'Неправильный порядковый номер зодиака {sign_zodiac}')
    # name_zodiac = zodiac_list[sign_zodiac - 1]
    # redirect_url = reverse('horoscope-name', args=[name_zodiac])
    # return HttpResponseRedirect(redirect_url)
    kianu_data = {
        'year_born': '2 сентября 1964 г.',
        'city_born': 'Бейрут, Ливан',
        'movie_name': 'На гребне волны', }
    return render(request, 'horoscope/kianu.html', context=kianu_data)
