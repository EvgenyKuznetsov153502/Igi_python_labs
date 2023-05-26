from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'telephone', 'date_of_birth', 'display_cars')
    # list_display = ('id', 'name')
    search_fields = ('name', 'telephone')


class PaymentInvoicesInline(admin.TabularInline):
    model = PaymentInvoice


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'brand', 'debt', 'display_client')
    # list_display = ('id', 'brand')
    search_fields = ('number', 'brand')
    list_filter = ('brand',)
    inlines = [PaymentInvoicesInline]


class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'price', 'is_occupied')
    search_fields = ('number',)
    list_filter = ('is_occupied',)


class PaymentInvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_number', 'price', 'enrollment', 'accrual_date', 'payment_date')
    search_fields = ('parking_number', 'id')
    list_filter = ('price', 'accrual_date', 'payment_date')


admin.site.register(Client, ClientAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(ParkingSpace, ParkingSpaceAdmin)
admin.site.register(PaymentInvoice, PaymentInvoiceAdmin)


