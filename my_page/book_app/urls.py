from django.urls import path, register_converter

from .views import index
#from .converters import SplitConverter
#register_converter(SplitConverter, 'split')

urlpatterns = [
    path('', index, name='book_app'),
]