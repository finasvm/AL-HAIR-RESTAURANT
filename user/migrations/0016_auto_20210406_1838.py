# Generated by Django 3.1.7 on 2021-04-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_person_welcome_coupan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Welcome_coupan',
            field=models.CharField(default=0, max_length=120),
        ),
    ]
