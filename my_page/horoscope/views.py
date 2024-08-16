from datetime import datetime, date

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class ZodiacSign:
    zodiac_sign_name_ru = ['Овен',    'Телец', 'Близнецы', 'Рак',   'Лев',  'Дева',  'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
    zodiac_sign_name_eng = ['aries', 'taurus', 'gemini',  'cancer', 'leon', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    zodiac_type_element_ru = ['Огонь', 'Земля', 'Воздух', 'Вода']
    zodiac_type_element_eng = ['fire', 'earth', 'air', 'water']
    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']

    def __init__(self, name_id, description: str, type_element_id: int, start_month: int, start_day: int,
                 end_month: int, end_day: int, order: int) -> None:
        self.name_id = name_id
        self.description = description
        self.type_element_id = type_element_id
        self.start_month = start_month
        self.start_day = start_day
        self.end_month = end_month
        self.end_day = end_day
        self.order = order

    def get_eng_name(self) -> str:
        return self.zodiac_sign_name_eng[self.order - 1]

    def get_ru_name(self) -> str:
        return self.zodiac_sign_name_ru[self.order - 1]

    def get_eng_type_element(self) -> str:
        return self.zodiac_type_element_eng[self.type_element_id - 1]

    def get_ru_type_element(self) -> str:
        return self.zodiac_type_element_ru[self.type_element_id - 1]

    def get_description(self) -> str:
        return self.description

    def get_start_date(self) -> str:
        return f'{self.months[self.start_month - 1]}, {self.start_day}'

    def get_end_date(self) -> str:
        return f'{self.months[self.end_month - 1]}, {self.end_day}'


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
            'aries': ZodiacSign(1, 'Первый знак зодиака, планета Марс', 1, 3, 21, 4, 20, 1),
            'taurus': ZodiacSign(2, 'Второй знак зодиака, планета Венера', 2, 4, 21, 5, 21, 2),
            'gemini': ZodiacSign(3, 'Третий знак зодиака, планета Меркурий', 3, 5, 22, 6, 21, 3),
            'cancer': ZodiacSign(4, 'Четвертый знак зодиака, Луна', 4, 6, 22, 7, 22, 4),
            'leon': ZodiacSign(5, 'Пятый знак зодиака, Солнце', 1, 7, 23, 8, 21, 5),
            'virgo': ZodiacSign(6, 'Шестой знак зодиака, планета Меркурий', 2, 8, 22, 9, 23, 6),
            'libra': ZodiacSign(7, 'Седьмой знак зодиака, планета Венера', 3, 9, 24, 10, 23, 7),
            'scorpio': ZodiacSign(8, 'Восьмой знак зодиака, планета Марс', 4, 10, 24, 11, 22, 8),
            'sagittarius': ZodiacSign(9, 'Девятый знак зодиака, планета Юпитер', 1, 11, 23, 12, 22, 9),
            'capricorn': ZodiacSign(10, 'Десятый знак зодиака, планета Сатурн', 2, 12, 23, 1, 20, 10),
            'aquarius': ZodiacSign(11, 'Одиннадцатый знак зодиака, планеты Уран и Сатурн', 3, 1, 21, 2, 19, 11),
            'pisces': ZodiacSign(12, 'Двенадцатый знак зодиака, планета Юпитер', 4, 2, 20, 3, 20, 12)
        }

    @staticmethod
    def horoscope_index(request: HttpRequest) -> HttpResponse:
        return render(request, 'horoscope/horoscope_index.html', {'title': 'Основное меню'})

    def horoscope_index_by_name(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'horoscope/horoscope_index_by_name.html', {'signs': self.signs, 'title': 'Выбор знака зодиака по названию'})

    def horoscope_index_by_type(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'horoscope/horoscope_index_by_type.html', {'type_elements': self.type_elements, 'title': 'Выбор знака зодиака по типу стихии'})

    def horoscope_by_type(self, request: HttpRequest, type_element: str) -> HttpResponse:
        if type_element in self.type_elements:
            return render(request, 'horoscope/horoscope_by_type.html',
                          {'signs': self.signs, 'type_element': type_element, 'title': 'Выбор знака зодиака по типу стихии'})
        return render(request, 'horoscope/unknown_element.html', {'type_element': type_element, 'title': 'Неизвестный тип стихии'})

    def get_horoscope_by_name(self, request: HttpRequest, sign: str) -> HttpResponse:
        zodiac = self.signs.get(sign)
        if zodiac:
            return render(request, 'horoscope/info_zodiac.html', {'zodiac': zodiac, 'title': 'Информация о знаке зодиака'})
        return render(request, 'horoscope/unknown_sign.html', {'zodiac': sign, 'title': 'Неизвестный знак зодиака'})

    def get_horoscope_by_number(self, request: HttpRequest, sign: int) -> HttpResponse:
        if sign < 1 or sign > len(self.signs.keys()):
            return render(request, 'horoscope/unknown_sign.html', {'zodiac': sign, 'title': 'Неизвестный знак зодиака'})
        zodiac_sign = list(self.signs.keys())[sign - 1]
        redirect_url = reverse('get_horoscope_by_name', args=[zodiac_sign])
        return HttpResponseRedirect(redirect_url)

    def get_horoscope_by_date(self, request: HttpRequest, month: int, day: int) -> HttpResponse:
        try:
            year = datetime.now().year
            date(year, month, day)
        except ValueError:
            return render(request, 'horoscope/unknown_date.html', {'month': month, 'day': day, 'title': 'Неизвестная дата'})
        for zodiac in self.signs.values():
            if (zodiac.start_month == month and zodiac.start_day <= day) or (
                    zodiac.end_month == month and zodiac.end_day >= day):
                zodiac_sign = zodiac.eng_name
                redirect_url = reverse('get_horoscope_by_name', args=[zodiac_sign])
                return HttpResponseRedirect(redirect_url)


horoscope = Horoscope()


