# Generated by Django 3.1.7 on 2021-03-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pinCode',
            field=models.PositiveIntegerField(),
        ),
    ]