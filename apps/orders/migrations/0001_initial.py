# Generated by Django 4.2 on 2023-10-11 23:42

import apps.orders.actions
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('not_payed', 'Not Payed'), ('earring', 'Earring'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='not_payed', max_length=50, verbose_name='Estado de pago de la orden')),
                ('order_status', models.CharField(choices=[('not_processed', 'Not Processed'), ('processed', 'Processed'), ('shipped', 'Shipping'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='not_processed', max_length=50, verbose_name='Estado de la orden')),
                ('order_number', models.CharField(db_index=True, default=apps.orders.actions.generate_transactionid, max_length=255, verbose_name='Numero de Orden')),
                ('country_region', models.CharField(choices=[('Cuba', 'Cuba')], default='Cuba', max_length=255, verbose_name='Pais')),
                ('full_name', models.CharField(max_length=255)),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(max_length=255)),
                ('address_line_3', models.CharField(blank=True, max_length=255, null=True)),
                ('number_house', models.CharField(blank=True, max_length=255, null=True)),
                ('building', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(choices=[('Pinar del Rio', 'Pinar Del Rio'), ('Artemisa', 'Artemisa'), ('Habana', 'Habana'), ('Mayabeque', 'Mayabeque'), ('Matanzas', 'Matanzas'), ('Villa Clara', 'Villa Clara'), ('Cienfuegos', 'Cienfuegos'), ('Sanctispíritus', 'Sanctispiritus'), ('Ciego de Avila', 'Ciego De Avila'), ('Camagüey', 'Camaguey'), ('Las Tunas', 'Las Tunas'), ('Granma', 'Granma'), ('Santiago de Cuba', 'Santiago De Cuba'), ('Holguín', 'Holguin'), ('Guantánamo', 'Guantanamo'), ('Isla de la Juventud', 'Isla De La Juventud')], max_length=255, verbose_name='Provincia')),
                ('municipality', models.CharField(max_length=255, verbose_name='Municipio')),
                ('shipping_time', models.CharField(max_length=255)),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_issued', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creada')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'Historial de orden',
                'verbose_name_plural': 'historical Ordenes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('not_payed', 'Not Payed'), ('earring', 'Earring'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='not_payed', max_length=50, verbose_name='Estado de pago de la orden')),
                ('order_status', models.CharField(choices=[('not_processed', 'Not Processed'), ('processed', 'Processed'), ('shipped', 'Shipping'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='not_processed', max_length=50, verbose_name='Estado de la orden')),
                ('order_number', models.CharField(default=apps.orders.actions.generate_transactionid, max_length=255, unique=True, verbose_name='Numero de Orden')),
                ('country_region', models.CharField(choices=[('Cuba', 'Cuba')], default='Cuba', max_length=255, verbose_name='Pais')),
                ('full_name', models.CharField(max_length=255)),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(max_length=255)),
                ('address_line_3', models.CharField(blank=True, max_length=255, null=True)),
                ('number_house', models.CharField(blank=True, max_length=255, null=True)),
                ('building', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(choices=[('Pinar del Rio', 'Pinar Del Rio'), ('Artemisa', 'Artemisa'), ('Habana', 'Habana'), ('Mayabeque', 'Mayabeque'), ('Matanzas', 'Matanzas'), ('Villa Clara', 'Villa Clara'), ('Cienfuegos', 'Cienfuegos'), ('Sanctispíritus', 'Sanctispiritus'), ('Ciego de Avila', 'Ciego De Avila'), ('Camagüey', 'Camaguey'), ('Las Tunas', 'Las Tunas'), ('Granma', 'Granma'), ('Santiago de Cuba', 'Santiago De Cuba'), ('Holguín', 'Holguin'), ('Guantánamo', 'Guantanamo'), ('Isla de la Juventud', 'Isla De La Juventud')], max_length=255, verbose_name='Provincia')),
                ('municipality', models.CharField(max_length=255, verbose_name='Municipio')),
                ('shipping_time', models.CharField(max_length=255)),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_issued', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creada')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
                'ordering': ['-date_issued'],
            },
        ),
        migrations.CreateModel(
            name='OrderPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('number_type', models.CharField(choices=[('Casa', 'Casa'), ('Movil Personal', 'Movil Personal'), ('Trabajo', 'Trabajo')], max_length=255, verbose_name='Tipo de numero')),
                ('contact_name', models.CharField(max_length=255, verbose_name='Nombre de contacto')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_number', to='orders.order', verbose_name='Perfil de Usuario')),
            ],
            options={
                'verbose_name': 'Numero telefonico de la Orden',
                'verbose_name_plural': 'Numeros telefonicos de las Ordenes',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad de productos')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order', verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'Producto de la Orden',
                'verbose_name_plural': 'Productos de las Ordenes',
            },
        ),
    ]
