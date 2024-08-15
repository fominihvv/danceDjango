from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('<int:post_number>/', detail_post_by_number, name='detail_post_by_number'),
    path('<str:post_name>/', detail_post_by_name, name='detail_post_by_name'),
]
