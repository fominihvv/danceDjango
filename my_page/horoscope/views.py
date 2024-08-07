from dataclasses import dataclass
from datetime import datetime, date

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


@dataclass
class ZodiacSign:
    eng_name: str
    ru_name: str
    description: str
    eng_type_element: str
    ru_type_element: str
    start_month: int
    start_day: int
    end_month: int
    end_day: int
    order: int


class Horoscope:
    __OBJ__ = None
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']
    type_elements = {'fire': 'Огонь', 'earth': 'Земля', 'air': 'Воздух', 'water': 'Вода'}

    def __new__(cls, *args, **kwargs) -> object:
        if cls.__OBJ__ is None:
            cls.__OBJ__ = object.__new__(cls)
        return cls.__OBJ__

    def __init__(self) -> None:
        self.signs = {
            'aries': ZodiacSign('aries', 'Овен', 'Первый знак зодиака, планета Марс', 'fire', 'огонь', 3, 21, 4, 20, 1),
            'taurus': ZodiacSign('taurus', 'Телец', 'Второй знак зодиака, планета Венера', 'earth', 'земля', 4, 21, 5,
                                 21, 2),
            'gemini': ZodiacSign('gemini', 'Близнецы', 'Третий знак зодиака, планета Меркурий', 'air', 'воздух', 5, 22,
                                 6, 21, 3),
            'cancer': ZodiacSign('cancer', 'Рак', 'Четвёртый знак зодиака, Луна', 'water', 'вода', 6, 22, 7, 22, 4),
            'leon': ZodiacSign('leon', 'Лев', 'Пятый знак зодиака, Солнце', 'fire', 'огонь', 7, 23, 8, 22, 5),
            'virgo': ZodiacSign('virgo', 'Дева', 'Шестой знак зодиака, планета Меркурий', 'earth', 'земля', 8, 23, 9,
                                22, 6),
            'libra': ZodiacSign('libra', 'Весы', 'Седьмой знак зодиака, планета Венера', 'air', 'воздух', 9, 23, 10, 22,
                                7),
            'scorpio': ZodiacSign('scorpio', 'Скорпион', 'Восьмой знак зодиака, планета Марс', 'water', 'вода', 10, 23,
                                  11, 21, 8),
            'sagittarius': ZodiacSign('sagittarius', 'Стрелец', 'Девятый̆ знак зодиака, планета Юпитер', 'fire',
                                      'огонь',
                                      11, 22, 12, 21, 9),
            'capricorn': ZodiacSign('capricorn', 'Козерог', 'Десятый знак зодиака, планета Сатурн', 'earth', 'земля',
                                    12, 22, 1, 19, 10),
            'aquarius': ZodiacSign('aquarius', 'Водолей', 'Одиннадцатый знак зодиака, планеты Уран и Сатурн', 'air',
                                   'воздух', 1, 20, 2, 18, 11),
            'pisces': ZodiacSign('pisces', 'Рыбы', 'Двенадцатый знак зодиака, планета Юпитер', 'water', 'вода', 2, 19,
                                 3, 20, 12)
        }

    @staticmethod
    def horoscope_index(request: HttpRequest) -> HttpResponse:
        head = '<h1>Знаки зодиака</h1>'
        body = ('<ul>' +
                f'<li><a href="{reverse("horoscope_index_by_name")}">По имени</a></li>' +
                f'<li><a href="{reverse("horoscope_index_by_type")}">По типу стихии</a></li>' +
                '</ul>')
        bottom = f'<br><p><a href="{reverse("global_index")}">Вернуться в основное меню</a></p>'
        return HttpResponse(head + body + bottom)

    def horoscope_index_by_name(self, request: HttpRequest) -> HttpResponse:
        head = '<h1>Выберите знак зодиака</h1>'
        body = '<ol>' + ''.join(
            f'<li><a href="{reverse("get_horoscope_by_name", args=[sign])}">{self.signs[sign].ru_name}</a></li>'
            for sign in self.signs) + '</ol>'
        bottom = f'<br><p><a href="{reverse("horoscope_index")}">Вернуться в меню</a></p>'
        return HttpResponse(head + body + bottom)

    @staticmethod
    def horoscope_index_by_type(request: HttpRequest) -> HttpResponse:
        head = '<h1>Выберите стихию</h1>'
        body = ('<ul>' +
                f'<li><a href="{reverse("horoscope_by_type", args=["fire"])}">Огонь</a></li>' +
                f'<li><a href="{reverse("horoscope_by_type", args=["earth"])}">Земля</a></li>' +
                f'<li><a href="{reverse("horoscope_by_type", args=["air"])}">Воздух</a></li>' +
                f'<li><a href="{reverse("horoscope_by_type", args=["water"])}">Вода</a></li>' +
                '</ul>')
        bottom = f'<br><p><a href="{reverse("horoscope_index")}">Вернуться в меню</a></p>'
        return HttpResponse(head + body + bottom)

    def horoscope_by_type(self, request: HttpRequest, type_element: str) -> HttpResponse:
        if type_element in self.type_elements:
            head = f'<h1>Выбрана стихия {self.type_elements[type_element]}</h1>'
            body = ('<ul>' +
                    ''.join(
                        f'<li><a href="{reverse("get_horoscope_by_name", args=[sign])}">'
                        f'{self.signs[sign].ru_name}</a></li>'
                        for sign in self.signs if self.signs[sign].eng_type_element == type_element)
                    + '</ul>')
            bottom = f'<br><p><a href="{reverse("horoscope_index_by_type")}">Вернуться в меню выбора стихии</a></p>'
            return HttpResponse(head + body + bottom)

        return HttpResponseNotFound(f'<h1>неизвестная стихия {type_element}</h1>')

    def get_horoscope_by_name(self, request: HttpRequest, sign: str) -> HttpResponse:
        zodiac = self.signs.get(sign)
        if zodiac is None:
            return HttpResponseNotFound(f'<h2>Неизвестный знак зодиака {sign}</h2>')
        head = f'<h1>{zodiac.ru_name}</h1>'
        body = (f'{zodiac.ru_name}. {zodiac.description}</br> c {self.months[zodiac.start_month - 1]}, '
                f'{zodiac.start_day} по {self.months[zodiac.end_month - 1]}, {zodiac.end_day}</br>')
        bottom = f'<br><p><a href="{reverse("horoscope_index_by_name")}">Вернуться к списку знаков зодиака</a></p>'
        return HttpResponse(head + body + bottom)

    def get_horoscope_by_number(self, request: HttpRequest, sign: int) -> HttpResponse:
        if sign < 1 or sign > len(self.signs.keys()):
            return HttpResponseNotFound(f'<h2>Неизвестный знак зодиака {sign}</h2>')
        zodiac_sign = list(self.signs.keys())[sign - 1]
        redirect_url = reverse('get_horoscope_by_name', args=[zodiac_sign])
        return HttpResponseRedirect(redirect_url)

    def get_horoscope_by_date(self, request: HttpRequest, month: int, day: int) -> HttpResponse:
        try:
            year = datetime.now().year
            date(year, month, day)
        except ValueError:
            return HttpResponseNotFound(f'<h2>Неверная дата. Месяц {month}, день {day}</h2>')
        for zodiac in self.signs.values():
            if (zodiac.start_month == month and zodiac.start_day <= day) or (
                    zodiac.end_month == month and zodiac.end_day >= day):
                zodiac_sign = zodiac.eng_name
                redirect_url = reverse('get_horoscope_by_name', args=[zodiac_sign])
                return HttpResponseRedirect(redirect_url)


horoscope = Horoscope()
