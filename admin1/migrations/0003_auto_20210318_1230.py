# Generated by Django 3.1.7 on 2021-03-18 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0002_auto_20210314_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='M_image',
            field=models.ImageField(upload_to='mainimage/'),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='main_image',
            field=models.ImageField(upload_to='f/'),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='s_image',
            field=models.ImageField(upload_to='ia/'),
        ),
    ]