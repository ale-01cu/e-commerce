# Generated by Django 4.2 on 2023-10-11 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_history', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Historial',
                'verbose_name_plural': 'Historial',
            },
        ),
        migrations.CreateModel(
            name='HistoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visited', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Visitado')),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_products', to='user_history.history', verbose_name='Historial')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_product', to='product.product', verbose_name='Productos')),
            ],
            options={
                'verbose_name': 'Historial de producto',
                'verbose_name_plural': 'Historial de productos',
                'ordering': ('-date_visited',),
            },
        ),
    ]
