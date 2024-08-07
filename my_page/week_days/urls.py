from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='week_days_index'),
    path('<int:weekday>/', get_task_by_weekday_number),
    path('<str:weekday>/', get_task_by_weekday_name, name='get_task_by_weekday_name'),

]
