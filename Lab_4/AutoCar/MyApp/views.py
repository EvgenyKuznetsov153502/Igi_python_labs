from django.db.models import F, Sum, Min
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from datetime import date
from .forms import *
from .models import Client, Car, ParkingSpace

# menu = ['Главная страница', 'Войти']
menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Клиенты", 'url_name': 'clients'},
    {'title': "Авто", 'url_name': 'cars'},
    {'title': "Парковочные места", 'url_name': 'parking_spaces'},
    {'title': "Долги", 'url_name': 'debts'}
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

        try:
            sp = car2.parking_space
            message = sp
        except:
            message = 'Нету'

        #print(message)

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
        'form': form,
        'message': message
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


def max_debt(request):
    try:
        list_of_clients_and_debts = []  # лист из листов вида [клиент, долг]

        cl = Client.objects.filter(cars__isnull=False).distinct()
        first_client = cl.first()
        id_max = first_client.pk
        temp = first_client.cars.aggregate(Sum('debt'))
        max_deb = temp['debt__sum']

        for client in cl:
            dict_sum = client.cars.aggregate(Sum('debt'))
            deb = dict_sum['debt__sum']
            temp_list = [client.name, deb]
            list_of_clients_and_debts.append(temp_list)
            if deb > max_deb:
                max_deb = deb
                id_max = client.pk
        max_debt_client = Client.objects.get(id=id_max)

        last_date = date(2000, 6, 1)
        for d in max_debt_client.cars.all():
            if d.invoices.all():
                temp_date = d.invoices.all().latest('payment_date').payment_date
                # print(temp_date)
                if temp_date > last_date:
                    last_date = temp_date

        # print(list_of_clients_and_debts)
        temp_dict_debt = Car.objects.aggregate(Min('debt'))
        min_debt = temp_dict_debt['debt__min']
        car_min = Car.objects.get(debt=min_debt)

    except:
        return HttpResponseNotFound("Ошибка чтения")

    context = {
        'title': 'Долги по клиентам',
        'menu': menu,
        'max_debt': max_deb,
        'max_debt_client': max_debt_client,
        'last_date': last_date,
        'list': list_of_clients_and_debts,
        'min_debt': min_debt,
        'car_min': car_min
    }
    return render(request, 'MyApp/debts.html', context=context)


def login(request):
    return render(request, 'MyApp/login.html', {'title': 'Авторизация', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


