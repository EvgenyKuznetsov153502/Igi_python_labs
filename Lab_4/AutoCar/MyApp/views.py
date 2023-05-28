from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from .models import Client, Car, ParkingSpace

# menu = ['Главная страница', 'Войти']
menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Клиенты", 'url_name': 'clients'},
    {'title': "Авто", 'url_name': 'cars'},
    {'title': "Парковочные места", 'url_name': 'parking_spaces'}
]


def home(request):
    num_of_clients = Client.objects.all().count()
    num_of_cars = Car.objects.all().count()
    spaces = ParkingSpace.objects.all()
    num_of_spaces = spaces.count()

    total_price = 0
    for s in spaces:
        total_price += s.price

    if num_of_spaces == 0:
        average_price = 0
    else:
        average_price = total_price / num_of_spaces

    context = {
        'title': 'Главная страница',
        'menu': menu,
        'num_of_clients': num_of_clients,
        'num_of_cars': num_of_cars,
        'average_price': average_price
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


def parking_spaces(request):
    spaces = ParkingSpace.objects.all()
    context = {
        'title': 'Список парковочных мест',
        'menu': menu,
        'spaces': spaces
    }
    return render(request, 'MyApp/park_spaces.html', context=context)


def show_park_space(request, sp_id):
    space = ParkingSpace.objects.filter(id=sp_id)
    context = {
        'title': 'Информация о парковочном месте',
        'menu': menu,
        'space': space
    }
    return render(request, 'MyApp/park_space_info.html', context=context)


def add_parking_space(request):
    context = {
        'title': 'Добавление парковочного места',
        'menu': menu
    }
    return render(request, 'MyApp/add_parking_space.html', context=context)


def login(request):
    return render(request, 'MyApp/login.html', {'title': 'Авторизация', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


