from django.http import HttpResponse, HttpRequest

from django.shortcuts import render
from random import sample

posts = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Если вы любите рыбалку, тогда Вам стоит приехать на Вуоксу! Только представьте, как приятно сидеть'
                   ' на берегу озера с удочкой, наслаждаться красотой окружающей природы, ароматом цветущих трав, '
                   'размышлять и предаваться мечтам. Даже если клюет плохо, а рыба ловится только мелкая - рыбалка '
                   'отличный вид медитации.'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': 'Пари́ж — столица и крупнейший город Франции. Находится на севере государства, в центральной части '
                   'Парижского бассейна, на реке Сена. Население — 2 102 650 человек (2023).'
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Финал Лиги чемпионов УЕФА 2022 прошёл 28 мая 2022 года. Это финал 67-го сезона главного турнира '
                   'среди европейских футбольных клубов под эгидой УЕФА и 30-го с момента...'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Что еще понадобится на успешной охоты на утку весной, кроме ружья, чучел, манка и скрадка?'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Полную программу «Дня огурца» в Суздале можно посмотреть на страницах фестиваля '
                   'на сайте Владимиро-Суздальского музея-заповедника .'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': '«Наше́ствие» — крупнейший в России фестиваль русского рока (а впоследствии и другой музыки) '
                   'под открытым небом. Основан радиостанцией «Наше радио».'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Кто придумал отмечать Новый год в ночь с 31 декабря на 1 января и как появился этот обычай, '
                   'когда праздник стал общенациональным торжеством... '
    },
]


def index(request: HttpRequest) -> HttpResponse:
    view_post_count = 4
    if len(posts) <= view_post_count:
        view_post_count = len(posts)
    return render(request, 'blog/index.html', {'title': 'Главная страница', 'posts': sample(posts, k=view_post_count)})


def detail_post_by_name(request: HttpRequest, post_name: str) -> HttpResponse:
    return render(request, 'blog/detail_by_name.html', {'post_name': post_name, 'title': post_name})


def detail_post_by_number(request: HttpRequest, post_number: int) -> HttpResponse:
    return render(request, 'blog/detail_by_number.html', {'post_number': post_number, 'title': post_number})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html', {'title': 'О нас'})
