from django.db import models
from django.contrib.auth.models import User
from admin1.models import *
# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    number = models.CharField(max_length=12)
    prof_Image = models.ImageField(upload_to='profpic/',null=True)
    Welcome_coupan = models.CharField(max_length=120 , default = 0)
    
    
    @property
    def User_image(self):
        if self.prof_Image == '':
            image = ''
        else:
            image = self.prof_Image.url
        return image

class Cart(models.Model):
    user = models.ForeignKey(Person,on_delete=models.CASCADE)
    products = models.ForeignKey(addProduct,on_delete=models.CASCADE )
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    Full_name = models.CharField(max_length=255)
    pinCode = models.PositiveIntegerField()
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    HouseName = models.CharField(max_length=150)
    landMark = models.CharField(max_length=150)
    user = models.ForeignKey(Person,on_delete=models.CASCADE)
class Order(models.Model):
    user_order = models.ForeignKey(Person,on_delete=models.CASCADE)
    Product = models.ForeignKey(addProduct,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Status = models.CharField(max_length=50)
    Qty = models.PositiveIntegerField()
    PaymentMethod = models.CharField(max_length=20)
    Date = models.DateField(auto_now_add=True)  

class WishList(models.Model):
    User_Product = models.ForeignKey(addProduct,on_delete=models.CASCADE)
    User_detail = models.ForeignKey(Person,on_delete=models.CASCADE)


class User_Profile(models.Model):
    User_Order = models.ForeignKey(Order,on_delete=models.CASCADE)
    User_Address = models.ForeignKey(Address,on_delete=models.CASCADE)
    User_Details = models.ForeignKey(Person,on_delete=models.CASCADE)
    User_Cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    User_wishlist = models.ForeignKey(WishList,on_delete=models.CASCADE)
    User_Image = models.ImageField(upload_to='profilepic/')

class Coupons(models.Model):
    Offer = models.IntegerField(default = 0)
    Coupon_code = models.CharField(max_length = 20)
    date = models.DateField(auto_now_add = True)
    Status = models.BooleanField(default=True)     

class Referal(models.Model):
    offerreferal = models.IntegerField(default = 0)
    refCoupon_code = models.CharField(max_length = 20)
    date = models.DateField(auto_now_add  = True)
    referaluser = models.ForeignKey(Person,on_delete=models.CASCADE)








