from django.db import models
from django.urls import reverse


class PaymentInvoice(models.Model):
    parking_number = models.IntegerField()
    price = models.IntegerField()  # цена за парковочное место
    enrollment = models.IntegerField(default=0)  # зачисление
    accrual_date = models.DateField(auto_now_add=True)  # дата выставления счета выставляется автомотически при создании
    payment_date = models.DateField(auto_now=True)  # дата последнего зачисления (выст. при ласт обновлении таблицы)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True, related_name='invoices')

    def __str__(self):
        return f"{self.pk}: [{self.accrual_date}] [{self.payment_date}]"

    class Meta:
        verbose_name = 'Счет на оплату'
        verbose_name_plural = 'Счета на оплату'
        ordering = ['id']


class ParkingSpace(models.Model):
    number = models.IntegerField(unique=True)  # номер парковочного места
    price = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    car = models.OneToOneField('Car', on_delete=models.SET_NULL, blank=True, null=True, related_name='parking_space')

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('parking_space', kwargs={'sp_id': self.pk})

    class Meta:
        verbose_name = 'Парковочное место'
        verbose_name_plural = 'Парковочные места'
        ordering = ['number']


class Car(models.Model):
    number = models.CharField(max_length=20)
    brand = models.CharField(max_length=70)  # марка авто
    clients = models.ManyToManyField('Client', related_name='cars')
    debt = models.IntegerField(default=0)  # долг на этой машине
    # space = models.OneToOneField(ParkingSpace, on_delete=models.SET_NULL)  # надо ли это поле тут

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_id': self.pk})

    def display_client(self):
        return ', '.join([client.name for client in self.clients.all()[:3]])

    display_client.short_description = 'Clients'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['id']


class Client(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    # cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client', kwargs={'client_id': self.pk})

    def display_cars(self):
        return ', '.join([car.number for car in self.cars.all()[:3]])

    display_cars.short_description = 'Cars'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']
