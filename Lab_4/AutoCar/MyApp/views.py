from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from .models import Client, Car

# menu = ['Главная страница', 'Войти']
menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Клиенты", 'url_name': 'clients'},
    {'title': "Авто", 'url_name': 'cars'}
]


def home(request):
    num_of_clients = Client.objects.all().count()
    num_of_cars = Car.objects.all().count()

    context = {
        'title': 'Главная страница',
        'menu': menu,
        'num_of_clients': num_of_clients,
        'num_of_cars': num_of_cars
    }

    return render(request, 'MyApp/home.html', context=context)


def clients(request):
    clien = Client.objects.all()
    context = {
        'title': 'Список клиентов',
        'menu': menu,
        'my_clients': clien
    }
    return render(request, 'MyApp/clients.html', context=context)


def show_client(request, client_id):
    cl = Client.objects.filter(id=client_id)

    context = {
        'title': 'Информация о клиенте',
        'menu': menu,
        'my_client': cl
    }
    return render(request, 'MyApp/client_info.html', context=context)


def cars(request):
    cars = Car.objects.all()
    context = {
        'title': 'Список автомобилей',
        'menu': menu,
        'my_cars': cars
    }
    return render(request, 'MyApp/cars.html', context=context)


def show_car(request, car_id):
    car = Car.objects.filter(id=car_id)
    context = {
        'title': 'Информация о автомобили',
        'menu': menu,
        'my_car': car
    }
    return render(request, 'MyApp/car_info.html', context=context)


def login(request):
    return render(request, 'MyApp/login.html', {'title': 'Авторизация', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


