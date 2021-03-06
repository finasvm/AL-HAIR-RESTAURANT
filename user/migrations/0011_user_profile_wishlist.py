# Generated by Django 3.1.7 on 2021-03-26 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0003_auto_20210318_1230'),
        ('user', '0010_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin1.addproduct')),
                ('User_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.person')),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Image', models.ImageField(upload_to='profilepic/')),
                ('Gender', models.CharField(max_length=15)),
                ('Age', models.PositiveIntegerField()),
                ('User_Address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address')),
                ('User_Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.cart')),
                ('User_Details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.person')),
                ('User_Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order')),
                ('User_wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.wishlist')),
            ],
        ),
    ]
