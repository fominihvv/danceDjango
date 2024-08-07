from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Здесь будет мой блог</h1>')


def index_posts(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Здесь будут посты</h1>')


def get_post_by_name(request: HttpRequest, posts: str) -> HttpResponse:
    return HttpResponse(f'<h1>Здесь содержится информация о посте {posts}</h1>')


def get_post_by_id(request: HttpRequest, number_post: int) -> HttpResponse:
    return HttpResponse(f'<h1>Здесь содержится информация о посте под номером {number_post}</h1>')