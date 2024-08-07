from django.http import HttpRequest, HttpResponse

pages = {'Гороскоп': 'horoscope', 'Дни недели': 'week_days', 'Геометрия': 'calculate_geometry'}


def index(request: HttpRequest) -> HttpResponse:
    result = ''.join(f'<h2><a href="/{pages[page]}">{page}</a><h2>' for page in pages)

    return HttpResponse('<h1>Главная страница</h1><br>' + result)
