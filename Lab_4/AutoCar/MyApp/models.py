import uuid

from django.db import models


class PaymentInvoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)  # ???
    parking_number = models.IntegerField()
    car_number = models.CharField(max_length=20)
    price = models.IntegerField()  # цена за парковочное место
    debt = models.IntegerField()  # долг на этой машине
    enrollment = models.IntegerField(default=0)  # зачисление
    accrual_date = models.DateField(auto_now_add=True)  # дата выставления счета
    payment_date = models.DateField(auto_now=True)  # дата последнего зачисления
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)  # ???

    def __str__(self):
        return self.id, self.car_number, self.debt  # ???? можно ли так


class ParkingSpace(models.Model):
    number = models.IntegerField()  # как сделать от 0 до 999
    price = models.IntegerField()
    is_occupied = models.BooleanField(default=True)
    car = models.OneToOneField('Car', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number


class Car(models.Model):
    number = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)  # марка авто
    # clients = models.ManyToManyField('Client')  # надо ли это поле тут
    # space = models.OneToOneField(ParkingSpace, on_delete=models.SET_NULL)  # надо ли это поле тут

    def __str__(self):
        return self.number


class Client(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.name

