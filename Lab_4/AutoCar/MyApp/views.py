from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404


# menu = ['Главная страница', 'Войти']
menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Войти", 'url_name': 'login'},
]


def home(request):

    context = {
        'title': 'Главная страница',
        'menu': menu
    }

    return render(request, 'MyApp/home.html', context=context)


def login(request):
    return render(request, 'MyApp/login.html', {'title': 'Авторизация', 'menu': menu} )


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