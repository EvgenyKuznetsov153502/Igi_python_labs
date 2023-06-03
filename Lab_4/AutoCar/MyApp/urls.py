from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/
    path('register/', register, name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('clients/', clients, name='clients'),
    path('clients/<int:client_id>', show_client, name='client'),
    path('cars/', cars, name='cars'),
    path('cars/<int:car_id>', show_car, name='car'),
    path('parking_spaces/', parking_spaces, name='parking_spaces'),
    path('parking_spaces/<int:sp_id>', show_park_space, name='parking_space'),
    path('parking_spaces/add', add_parking_space, name='add_parking_space'),
    path('parking_spaces/<int:sp_id>/delete', delete_park_space, name='delete_park_space'),
    path('debts/', max_debt, name='debts'),
    path('logout/', logout_user, name='logout')
    # path('cars/<int:carid>/', cars),  # http://127.0.0.1:8000/cars/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/cars/
]
