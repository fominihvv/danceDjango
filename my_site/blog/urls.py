from django.urls import path

from .views import *

urlpatterns = [
    path('', index_posts),
    path('<int:number_post>/', get_post_by_id),
    path('<str:posts>/', get_post_by_name),
]
