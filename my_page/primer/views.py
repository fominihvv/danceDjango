from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def primer_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'primer/primer_base.html')
