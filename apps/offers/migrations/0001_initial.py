# Generated by Django 4.2 on 2023-10-11 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre de la oferta')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
                ('start_date', models.DateTimeField(verbose_name='Fecha del inicio de la oferta')),
                ('end_date', models.DateTimeField(verbose_name='Fecha del fin de la oferta')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
            },
        ),
        migrations.CreateModel(
            name='OfferProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(choices=[('%', 'Porciento'), ('$', 'Dinero')], max_length=12, verbose_name='Tipo de descuento')),
                ('discount', models.FloatField(verbose_name='Descuento')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_product', to='offers.offer', verbose_name='Oferta')),
            ],
            options={
                'verbose_name': 'Oferta del producto',
                'verbose_name_plural': 'Ofertas de los productos',
            },
        ),
    ]