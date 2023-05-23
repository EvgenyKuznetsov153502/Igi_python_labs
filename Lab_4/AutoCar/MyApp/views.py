from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404


def home(request):  # HttpRequest
    return HttpResponse("Страница приложения  AutoCar.")


def cars(request, carid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Список автомобилей</h1><p>{carid}</p>")


def archive(request, year):
    if int(year) > 2023:
        return redirect('home')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')