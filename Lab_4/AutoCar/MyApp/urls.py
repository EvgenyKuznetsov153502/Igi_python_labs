from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/
    path('login/', login, name='login'),
    path('clients/', clients, name='clients'),
    path('client/<int:client_id>', show_client, name='client'),
    path('cars/', cars, name='cars'),
    path('car/<int:car_id>', show_car, name='car')


    # path('cars/<int:carid>/', cars),  # http://127.0.0.1:8000/cars/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/cars/
]
