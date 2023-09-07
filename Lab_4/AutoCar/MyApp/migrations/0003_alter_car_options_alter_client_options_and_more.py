# Generated by Django 4.2.1 on 2023-05-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_remove_client_cars_remove_paymentinvoice_car_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['id'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['name'], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='parkingspace',
            options={'ordering': ['number'], 'verbose_name': 'Парковочное место', 'verbose_name_plural': 'Парковочные места'},
        ),
        migrations.AlterModelOptions(
            name='paymentinvoice',
            options={'ordering': ['id'], 'verbose_name': 'Счет на оплату', 'verbose_name_plural': 'Счета на оплату'},
        ),
        migrations.AlterField(
            model_name='parkingspace',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
