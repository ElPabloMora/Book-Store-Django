# Generated by Django 5.0.3 on 2024-05-14 20:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_libro_special_price_alter_carrito_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('special_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('count_sale', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
