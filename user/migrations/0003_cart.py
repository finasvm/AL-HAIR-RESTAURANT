# Generated by Django 3.1.7 on 2021-03-18 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0003_auto_20210318_1230'),
        ('user', '0002_person_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('count', models.PositiveIntegerField(default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin1.addproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.person')),
            ],
        ),
    ]
