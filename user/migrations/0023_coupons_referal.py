# Generated by Django 3.1.7 on 2021-04-09 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_person_welcome_coupan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Offer', models.IntegerField(default=0)),
                ('Coupon_code', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerreferal', models.IntegerField(default=0)),
                ('refCoupon_code', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('referaluser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.person')),
            ],
        ),
    ]
