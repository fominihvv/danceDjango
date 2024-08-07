from dataclasses import dataclass
from math import pi

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse


@dataclass
class Rectangle:
    width: int | float
    height: int | float

    def __post_init__(self) -> None:  self.area = self.width * self.height


@dataclass
class Square:
    side: int | float

    def __post_init__(self) -> None: self.area = self.side ** 2


@dataclass
class Circle:
    radius: int | float

    def __post_init__(self) -> None: self.area = pi * (self.radius ** 2)


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Расчёт площади геометрических фигур</h1>')


def rectangle_area(request: HttpRequest, width: int, height: int) -> HttpResponse:
    return HttpResponse(
        f'<h1>Площадь прямоугольника размером {width}x{height} равна {Rectangle(width, height).area}</h1>')


def square_area(request: HttpRequest, width: int) -> HttpResponse:
    return HttpResponse(f'<h1>Площадь квадрата размером {width}x{width} равна {Square(width).area}</h1>')


def circle_area(request: HttpRequest, radius: int) -> HttpResponse:
    return HttpResponse(f'<h1>Площадь круга с радиусом {radius} равна {Circle(radius).area:.2f}</h1>')


def get_rectangle_area(request: HttpRequest, width: int, height: int) -> HttpResponse:
    redirect_url = reverse('rectangle_area', args=[width, height])
    return HttpResponseRedirect(redirect_url)


def get_square_area(request: HttpRequest, width: int) -> HttpResponse:
    redirect_url = reverse('square_area', args=[width])
    return HttpResponseRedirect(redirect_url)


def get_circle_area(request: HttpRequest, radius: int) -> HttpResponse:
    redirect_url = reverse('circle_area', args=[radius])
    return HttpResponseRedirect(redirect_url)
