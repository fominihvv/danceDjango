from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='geometry'),
    path('rectangle/<int:width>/<int:height>', rectangle_area, name='rectangle_area'),
    path('circle/<int:radius>', circle_area, name='circle_area'),
    path('square/<int:width>', square_area, name = 'square_area'),
    path('get_rectangle_area/<int:width>/<int:height>', get_rectangle_area),
    path('get_circle_area/<int:radius>', get_circle_area),
    path('get_square_area/<int:width>', get_square_area),
]