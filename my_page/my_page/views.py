from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

projects = {'Гороскоп': 'horoscope', 'Дни недели': 'week_days', 'Геометрия': 'geometry'}


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'projects.html', {'title': 'Основное меню', 'projects': projects})
