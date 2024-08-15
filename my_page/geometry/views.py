from dataclasses import dataclass
from math import pi

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

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
    return render(request, 'geometry/rectangle.html', {'width': width, 'height': height, 'area': width * height})


def square_area(request: HttpRequest, width: int) -> HttpResponse:
    return render(request, 'geometry/square.html', {'width': width, 'area': width ** 2})


def circle_area(request: HttpRequest, radius: int) -> HttpResponse:
    return render(request, 'geometry/circle.html', {'radius': radius, 'area': pi * (radius ** 2)})


def get_rectangle_area(request: HttpRequest, width: int, height: int) -> HttpResponse:
    redirect_url = reverse('rectangle_area', args=[width, height])
    return HttpResponseRedirect(redirect_url)


def get_square_area(request: HttpRequest, width: int) -> HttpResponse:
    redirect_url = reverse('square_area', args=[width])
    return HttpResponseRedirect(redirect_url)


def get_circle_area(request: HttpRequest, radius: int) -> HttpResponse:
    redirect_url = reverse('circle_area', args=[radius])
    return HttpResponseRedirect(redirect_url)
