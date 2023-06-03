from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import F, Sum, Min
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from datetime import date, datetime
from django.contrib.auth.decorators import user_passes_test
from django.templatetags import tz
from django.urls import reverse_lazy
import requests

from .forms import *
from .models import Client, Car, ParkingSpace


def get_ip_request():

    ip_request = requests.get('http://ip-api.com/json/')
    current_date = date.today()
    if ip_request.status_code == 200:
        ip_request = ip_request.json()
        time_zone = ip_request['timezone']
        current_date = date.today()
    else:
        time_zone = 'Не определен'
    return {'zone': time_zone, 'cur_date': current_date }


def get_bitkoin():
    ip_request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if ip_request.status_code == 200:
        ip_request = ip_request.json()
        bpi = ip_request['bpi']
        USD = bpi['USD']
        EUR = bpi['EUR']
        bit_rate_usd = USD['rate']
        bit_rate_eur = EUR['rate']
    else:
        bit_rate_usd = 'Не определен'
        bit_rate_eur = 'Не определен'
    return {'USD': bit_rate_usd, 'EUR': bit_rate_eur}


def is_admin(user):
    return user.is_superuser


menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Регистрация", 'url_name': 'register'},
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Клиенты", 'url_name': 'clients'},
    {'title': "Авто", 'url_name': 'cars'},
    {'title': "Парковочные места", 'url_name': 'parking_spaces'},
    {'title': "Долги", 'url_name': 'debts'},
    {'title': "Выйти", 'url_name': 'logout'}
]


def get_menu(request):
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        new_menu = [  # для незарегистрированных
            {'title': "Главная страница", 'url_name': 'home'},
            {'title': "Регистрация", 'url_name': 'register'},
            {'title': "Войти", 'url_name': 'login'}
        ]
    elif request.user.is_staff:
        new_menu = [  # для адмниа
            {'title': "Главная страница", 'url_name': 'home'},
            {'title': "Клиенты", 'url_name': 'clients'},
            {'title': "Авто", 'url_name': 'cars'},
            {'title': "Парковочные места", 'url_name': 'parking_spaces'},
            {'title': "Долги", 'url_name': 'debts'},
            {'title': "Выйти", 'url_name': 'logout'}
        ]
    else:
        new_menu = [  # для зарегистрированных
            {'title': "Главная страница", 'url_name': 'home'},
            {'title': "Личный кабинет", 'url_name': 'personal_account'},
            {'title': "Выйти", 'url_name': 'logout'}
        ]
    return new_menu


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

    new_menu = get_menu(request)
    context = {
        'title': 'Главная страница',
        'menu': new_menu,
        'num_of_clients': num_of_clients,
        'num_of_cars': num_of_cars,
        'average_price': average_price
    }

    return render(request, 'MyApp/home.html', context=context)


@user_passes_test(is_admin)
def clients(request):
    clien = Client.objects.all()
    new_menu = get_menu(request)
    context = {
        'title': 'Список клиентов',
        'menu': new_menu,
        'my_clients': clien
    }
    return render(request, 'MyApp/clients.html', context=context)


@user_passes_test(is_admin)
def show_client(request, client_id):
    cl = Client.objects.filter(id=client_id)
    new_menu = get_menu(request)
    context = {
        'title': 'Информация о клиенте',
        'menu': new_menu,
        'my_client': cl
    }
    return render(request, 'MyApp/client_info.html', context=context)


@user_passes_test(is_admin)
def cars(request):
    cars = Car.objects.all()
    new_menu = get_menu(request)
    context = {
        'title': 'Список автомобилей',
        'menu': new_menu,
        'my_cars': cars
    }
    return render(request, 'MyApp/cars.html', context=context)


@login_required(login_url='home')
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
    new_menu = get_menu(request)
    context = {
        'title': 'Информация об автомобиле',
        'menu': new_menu,
        'my_car': car,
        'spaces': spaces,
        'id': car_id,
        'form': form,
        'message': message
    }
    return render(request, 'MyApp/car_info.html', context=context)


@user_passes_test(is_admin)
def parking_spaces(request):
    spaces = ParkingSpace.objects.all()
    new_menu = get_menu(request)
    context = {
        'title': 'Список парковочных мест',
        'menu': new_menu,
        'spaces': spaces
    }
    return render(request, 'MyApp/park_spaces.html', context=context)


@user_passes_test(is_admin)
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
    new_menu = get_menu(request)
    context = {
        'title': 'Информация о парковочном месте',
        'menu': new_menu,
        'space': space,
        'form': form,
        'id': sp_id
    }
    return render(request, 'MyApp/park_space_info.html', context=context)


@user_passes_test(is_admin)
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
    new_menu = get_menu(request)
    context = {
        'title': 'Добавление парковочного места',
        'menu': new_menu,
        'form': form
    }
    return render(request, 'MyApp/add_parking_space.html', context=context)


@user_passes_test(is_admin)
def delete_park_space(request, sp_id):
    try:
        sp = ParkingSpace.objects.get(id=sp_id)
        sp.delete()
        return redirect('parking_spaces')
    except:
        return HttpResponseNotFound("<h2>Ошибка удаления</h2>")


@user_passes_test(is_admin)
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
    new_menu = get_menu(request)
    context = {
        'title': 'Долги по клиентам',
        'menu': new_menu,
        'max_debt': max_deb,
        'max_debt_client': max_debt_client,
        'last_date': last_date,
        'list': list_of_clients_and_debts,
        'min_debt': min_debt,
        'car_min': car_min
    }
    return render(request, 'MyApp/debts.html', context=context)


def register(request):
    # form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                print(form.cleaned_data)
                login = form.cleaned_data['login']
                password = form.cleaned_data['password1']
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                telephone = form.cleaned_data['telephone']
                date_of_birth = form.cleaned_data['date_of_birth']
                user = User()
                client = Client()
                user.username = login
                user.email = email
                user.set_password(password)
                client.name = name
                client.telephone = telephone
                client.date_of_birth = date_of_birth
                client.user = user
                user.save()
                client.save()
                return redirect('login')
            except:
                form.add_error(None, 'Ошибка регистрации')

    else:
        form = RegisterUserForm()

    new_menu = get_menu(request)
    context = {
        'title': 'Регистрация',
        'menu': new_menu,
        'form': form
    }

    return render(request, 'MyApp/register.html', context=context)


menu_for_reg = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Регистрация", 'url_name': 'register'},
    {'title': "Войти", 'url_name': 'login'}
]


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'MyApp/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_for_reg
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='home')
def personal_account(request):
    user = request.user
    if hasattr(user, 'client'):
        cars = user.client.cars.all()
    else:
        raise Http404()
    ip_date = get_ip_request()
    zone = ip_date['zone']
    cur_date = ip_date['cur_date']
    bit = get_bitkoin()
    USD = bit['USD']
    EUR = bit['EUR']
    print(USD,EUR)
    new_menu = get_menu(request)
    context = {
        'title': 'Личный кабинет',
        'menu': new_menu,
        'my_cars': cars,
        'user_name': user.username,
        'zone': zone,
        'cur_date': cur_date,
        'USD': USD,
        'EUR': EUR
    }
    return render(request, 'MyApp/personal_account.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


