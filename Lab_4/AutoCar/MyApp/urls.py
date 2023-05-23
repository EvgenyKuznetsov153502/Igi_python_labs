from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/
    path('cars/<int:carid>/', cars),  # http://127.0.0.1:8000/cars/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/cars/
]
