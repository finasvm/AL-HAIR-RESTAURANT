from django.db import models

# Create your models here.

class add_Category(models.Model):
    category = models.TextField()
    discount = models.IntegerField(default=0)

class addProduct(models.Model):
    p_name = models.CharField(max_length=255)
    p_desc = models.TextField()
    p_cate = models.ForeignKey(add_Category,on_delete=models.CASCADE)
    p_price = models.DecimalField(decimal_places =2, max_digits =10)
    M_image = models.ImageField(upload_to='mainimage/')
    s_image = models.ImageField(upload_to='ia/')
    main_image = models.ImageField(upload_to='f/')

    @property
    def discountprice(self):
        discount1 = (self.p_price/100) * self.p_cate.discount
        discountedprice =  self.p_price - discount1
        return discountedprice

    @property  
    def ImageURL(self):
        try:
            url = self.M_image.url
        except:
            url = ''
        return url
    @property
    def imageurl1(self):
        if self.M_image == '':
            image = ''
        else:
            image = self.M_image.url
        return image

    @property
    def imageurl2(self):
        if self.s_image == '':
            image = ''
        else:
            image = self.s_image.url
        return image

    @property
    def imageurl3(self):
        if self.main_image == '':
            image = ''
        else:
            image = self.main_image.url
        return image



