from django.db.models import F
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404

from .forms import *
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
    try:
        car2 = Car.objects.get(id=car_id)
        spaces = car2.invoices.all()
    except:
        return HttpResponseNotFound("<h2>Нету машины с таким id</h2>")

    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            try:
                money = form.cleaned_data['enrollment']
                car2.debt -= money
                car2.save()
                last_inv = spaces.last()
                last_inv.enrollment += money
                last_inv.save()
                return redirect('car', car_id)
            except:
                form.add_error(None, 'Ошибка оплаты')
    else:
        form = PayForm()

    context = {
        'title': 'Информация об автомобиле',
        'menu': menu,
        'my_car': car,
        'spaces': spaces,
        'id': car_id,
        'form': form
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

    if request.method == 'POST':
        form = UpdatePrice(request.POST)
        if form.is_valid():
            try:
                price = form.cleaned_data['price']
                sp = ParkingSpace.objects.get(id=sp_id)
                sp.price = price
                sp.save()
                return redirect('parking_space', sp_id)
            except:
                form.add_error(None, 'Ошибка изменения цены')
    else:
        form = UpdatePrice()

    context = {
        'title': 'Информация о парковочном месте',
        'menu': menu,
        'space': space,
        'form': form,
        'id': sp_id
    }
    return render(request, 'MyApp/park_space_info.html', context=context)


def add_parking_space(request):
    # form = AddParkSpace()
    if request.method == "POST":
        form = AddParkSpace(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('parking_spaces')
    else:
        form = AddParkSpace()
    context = {
        'title': 'Добавление парковочного места',
        'menu': menu,
        'form': form
    }
    return render(request, 'MyApp/add_parking_space.html', context=context)


def delete_park_space(request, sp_id):
    try:
        sp = ParkingSpace.objects.get(id=sp_id)
        sp.delete()
        return redirect('parking_spaces')
    except:
        return HttpResponseNotFound("<h2>Ошибка удаления</h2>")


def login(request):
    return render(request, 'MyApp/login.html', {'title': 'Авторизация', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


