# Generated by Django 4.2 on 2023-10-11 23:42

import apps.category.actions
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
                ('photo', models.ImageField(null=True, upload_to=apps.category.actions.generate_category_photo_path, verbose_name='Foto de Categoria')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
