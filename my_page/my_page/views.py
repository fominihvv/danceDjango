from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

projects = {'Гороскоп': 'horoscope', 'Дни недели': 'week_days', 'Геометрия': 'geometry', 'Кинопоиск': 'movie_app', 'Книжный магазин': 'book_app'}


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'projects.html', {'title': 'Основное меню', 'projects': projects})
