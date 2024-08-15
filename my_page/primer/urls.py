from django.urls import path
from .views import primer_index

urlpatterns = [
    path('', primer_index, name='primer_index'),
]