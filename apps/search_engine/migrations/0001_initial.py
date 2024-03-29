# Generated by Django 4.2 on 2023-10-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Searches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', models.CharField(max_length=255, verbose_name='Texto de la busqueda')),
                ('processed_search_text', models.CharField(max_length=255, verbose_name='Texto de la busqueda procesado')),
                ('number_searches', models.PositiveIntegerField(default=1, verbose_name='Numero de busquedas')),
                ('last_time_searched', models.DateTimeField(auto_now=True, verbose_name='Fecha de creado')),
            ],
            options={
                'verbose_name': 'Busqueda',
                'verbose_name_plural': 'Busquedas',
                'ordering': ('-number_searches',),
            },
        ),
    ]
