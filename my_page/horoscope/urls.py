from django.urls import path, register_converter

from .views import horoscope
#from .converters import SplitConverter
#register_converter(SplitConverter, 'split')

urlpatterns = [
    path('', horoscope.horoscope_index, name='horoscope'),
    path('horoscope_index_by_name/', horoscope.horoscope_index_by_name, name='horoscope_index_by_name'),
    path('horoscope_index_by_type/', horoscope.horoscope_index_by_type, name='horoscope_index_by_type'),
    path('type/', horoscope.horoscope_index_by_type),
    path('type/<str:type_element>', horoscope.horoscope_by_type, name='horoscope_by_type'),
    path('name/<int:sign>/', horoscope.get_horoscope_by_number),
    path('name/<str:sign>/', horoscope.get_horoscope_by_name, name='get_horoscope_by_name'),
    path('horoscope/<int:month>/<int:day>/', horoscope.get_horoscope_by_date, name='get_horoscope_by_date'),
    path('name/', horoscope.horoscope_index_by_name),
]
