# Generated by Django 4.2 on 2023-10-11 23:42

import apps.product.actions
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre de la marca')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Measure_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
                ('symbol', models.CharField(max_length=5, unique=True, verbose_name='Simbolo de medida')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de Medidas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
                ('photo', models.ImageField(upload_to=apps.product.actions.generate_product_photo_path, verbose_name='Foto')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('keywords', models.CharField(max_length=255, verbose_name='Palabras claves')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.brand', verbose_name='Marca')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='category.category', verbose_name='Categoria')),
                ('measure_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product', to='product.measure_unit', verbose_name='Unidad de medida')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to=apps.product.actions.generate_product_images_path, verbose_name='Url de la Imagen')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='product.product', verbose_name='Prodduto')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Nombre')),
                ('photo', models.TextField(max_length=100, verbose_name='Foto')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('keywords', models.CharField(max_length=255, verbose_name='Palabras claves')),
                ('create_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creado')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('brand', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='product.brand', verbose_name='Marca')),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='category.category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'historical Producto',
                'verbose_name_plural': 'historical Productos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
