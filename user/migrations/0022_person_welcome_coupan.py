# Generated by Django 3.1.7 on 2021-04-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_remove_person_welcome_coupan'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Welcome_coupan',
            field=models.CharField(default=0, max_length=120),
        ),
    ]
