from django.db import models


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
    number = models.IntegerField()
    price = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    car = models.OneToOneField('Car', on_delete=models.SET_NULL, null=True, related_name='parking_space')

    def __str__(self):
        return str(self.number)

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

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']
