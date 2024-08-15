from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

week_days = {'monday': 'Понедельник', 'tuesday': 'Вторник', 'wednesday': 'Среда', 'thursday': 'Четверг',
             'friday': 'Пятница', 'saturday': 'Суббота', 'sunday': 'Воскресенье'}


def index(request: HttpRequest) -> HttpResponse:
    response = render_to_string('week_days/greeting.html')
    return HttpResponse(response)


def get_task_by_weekday_name(request: HttpRequest, weekday: str) -> HttpResponse:
    task_day = week_days.get(weekday, None)
    if task_day is None:
        return HttpResponseNotFound(f'<h1>неизвестный день недели {weekday}</h1>')
    return HttpResponse(f'<h1>задачи на {task_day}</h1>')


def get_task_by_weekday_number(request: HttpRequest, weekday: int) -> HttpResponse:
    if weekday < 1 or weekday > len(week_days):
        return HttpResponseNotFound(f'<h1>неизвестный день недели {weekday}</h1>')
    task_day = list(week_days.keys())[weekday - 1]
    redirect_url = reverse('get_task_by_weekday_name', args=[task_day])
    return HttpResponseRedirect(redirect_url)
