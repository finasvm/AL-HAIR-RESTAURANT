# Generated by Django 3.1.7 on 2021-03-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
