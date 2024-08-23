from django.urls import path, register_converter

from .views import index, movie_detail
#from .converters import SplitConverter
#register_converter(SplitConverter, 'split')

urlpatterns = [
    path('', index, name='movie_app'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
]
