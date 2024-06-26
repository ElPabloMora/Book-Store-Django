# Generated by Django 5.0.3 on 2024-05-11 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_libro_count_sale_libro_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='special_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to='products.libro'),
        ),
    ]
