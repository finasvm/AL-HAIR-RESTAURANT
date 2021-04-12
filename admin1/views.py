from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from user.models import Person,Order,Coupons
from admin1.models import addProduct,add_Category
from django.core.files import File
import base64
from django.core.files.base import ContentFile
from datetime import date
import datetime
import xlrd

# Create your views here.
def adlogin(request):
    if request.session.has_key('key'):
        return redirect(adpanel)
    else:
        if request.method =='POST':
            username=request.POST["username"]
            password=request.POST["password"]
            if (username =="finasvm" and password =="1234"):
                request.session['key'] = 'sir'
                return JsonResponse('true', safe=False)
                #return redirect(userdata)
            else:
                #messages.info(request,'INVALID DATAS')
                return JsonResponse('false', safe=False)
                return redirect(adlogin)

        else:
            return render(request,'admin/adlogin.html')

def adpanel(request):
    if request.session.has_key('key'):
        order = Order.objects.all()
        qty = order.count()
        orderdelivered = Order.objects.filter(Status='delivered')
        qtydelievered = orderdelivered.count()
        totalcustomers = User.objects.all()
        qtycustomers = totalcustomers.count()
        revenue=0
        for i in orderdelivered:
            revenue += i.Price
        netrevenue=revenue
        currentDate = date.today()
        currentmonth = currentDate.month
        print(currentmonth)
        orderdate = Order.objects.filter(Date__month=currentmonth,Status='delivered')
        revenue1=0
        for i in orderdate:
            revenue1 = revenue1 + i.Price
        revenuemonth = revenue1
        currentyear = currentDate.year
        orderyear = Order.objects.filter(Date__year=currentyear,Status='delivered')
        revenue2=0
        for i in orderyear:
            revenue2 = revenue2 + i.Price
        revenueyear = revenue2
        ordertoday = Order.objects.filter(Date__day=currentDate.day,Status='delivered')
        revenue3=0
        for i in ordertoday:
            revenue3 = revenue3 + i.Price
        revenuetoday = revenue3
        a = date(date.today().year, 1,1)
        january=a.month     
        context = {'qty':qty,'qtydelivered':qtydelievered,'qtycustomers':qtycustomers,'totalsum':netrevenue,'revenuemonth':revenuemonth,'revenueyear':revenueyear,'revenuetoday':revenuetoday}
        return render(request,'admin/adpanel.html',context)
    else:
        return redirect(adlogin)

def usertable(request):
    if request.session.has_key('key'):
        users= Person.objects.all()
        return render(request,'admin/usertable.html',{'users' : users})
    else:
        return redirect(adlogin)
def block(request,pk):
    if request.session.has_key('key'):
        current_user = Person.objects.get(id=pk)
        user=User.objects.get(id=current_user.user_id)
        if user.is_active == True:
            user.is_active = False
            user.save()
            return redirect(usertable)
        else:
            user.is_active = True
            user.save()
            return redirect(usertable)
    else:
        return redirect(adlogin)

def viewproduct(request):
    if request.session.has_key('key'):
        prod = addProduct.objects.all()
        return render(request,'admin/viewproduct.html',{'prod': prod})
    else:
        return redirect(adlogin)
def deletepro(request,pk):
    if request.session.has_key('key'):
        pro = addProduct.objects.get(id=pk)
        pro.delete()
        return redirect('viewproduct') 
    else:
        return redirect(adlogin) 

def editpro(request,pk):
    if request.session.has_key('key'):
        prod = addProduct.objects.get(id=pk)
        cat1 = add_Category.objects.all()
        catpro = {'prod':prod,'cat':cat1}
        if request.method =='POST' :
            print('helooo')
            p_name=request.POST['pro_name']
            prod.p_name = p_name
            prod.p_desc=request.POST['pro_desc']
            cate=request.POST['p_cate']
            cat = add_Category.objects.get(category=cate)
            prod.p_cate=cat
            prod.p_price=request.POST['p_price']
            image1=request.POST['imageurl1']
            image2=request.POST['imageurl2']
            image3=request.POST['imageurl3']
            if  image1 == '' or  image2 == '' or  image3 == '': 
                messages.info(request,'you should crop the images')
                return redirect(toadd)
            else:
                format, imgstr1 = image1.split(';base64,')
                ext = format.split('/')[-1]
                img1 = ContentFile(base64.b64decode(imgstr1),name=p_name+ '.' + ext)
                
                format, imgstr2 =  image2.split(';base64,')
                ext1 = format.split('/')[-1]
                img2 = ContentFile(base64.b64decode(imgstr2),name=p_name+ '.' + ext1)
                
                format, imgstr3 =  image3.split(';base64,')
                ext2 = format.split('/')[-1]
                img3 = ContentFile(base64.b64decode(imgstr3),name=p_name+ '.' + ext2)
                
                prod.M_image = img1
                prod.s_image = img2
                prod.main_image = img3

            prod.save()

            return redirect('viewproduct')
        
        else:
            return render(request,'admin/editpro.html',catpro)
    else:
        return redirect(adlogin)



def addproduct(request):
    if request.session.has_key('key'):
        categ=add_Category.objects.all()
        return render(request,'admin/addproduct.html',{'categ': categ})
    else:
        return redirect(adlogin)

def toadd(request):
    if request.session.has_key('key'):
        if request.method =='POST' :
            print('helooo')
            p_name=request.POST['pro_name']
            p_desc=request.POST['pro_desc']
            p_cate=request.POST['p_cate']
            p_price=request.POST['p_price']
            image1=request.POST['imageurl1']
            image2=request.POST['imageurl2']
            image3=request.POST['imageurl3']
            if image1 == '' or image2 == '' or image3 == '': 
                messages.info(request,'you should crop the images')
                return redirect(toadd)
            else:
                format, imgstr1 = image1.split(';base64,')
                ext = format.split('/')[-1]
                img1 = ContentFile(base64.b64decode(imgstr1),name=p_name+ '.' + ext)
                
                format, imgstr2 = image2.split(';base64,')
                ext1 = format.split('/')[-1]
                img2 = ContentFile(base64.b64decode(imgstr2),name=p_name+ '.' + ext1)
                
                format, imgstr3 = image3.split(';base64,')
                ext2 = format.split('/')[-1]
                img3 = ContentFile(base64.b64decode(imgstr3),name=p_name+ '.' + ext2)

            if addProduct.objects.filter(p_name=p_name).exists():
                messages.info(request,'category already exist')
            else:
                category = add_Category.objects.get(category=p_cate)
                addproduct = addProduct.objects.create(p_name=p_name,p_desc=p_desc,p_cate=category,p_price=p_price,M_image=img1,s_image=img2,main_image=img3)
                addproduct.save()
                return redirect('viewproduct')
        
        else:
            categ=add_Category.objects.all()
            return render(request,'admin/addproduct.html',{'categ':categ})
    else:
        return redirect(adlogin)

def addcategory(request):
    if request.session.has_key('key'):
        return render(request,'admin/addcategory.html')
    else:
        return redirect(adlogin)

def addedcategory(request):
    if request.session.has_key('key'):

        if request.method == 'POST':
            print('efeek')
            category=request.POST['category']
            if add_Category.objects.filter(category=category).exists():
                messages.info(request,'category already exist')
            else:
                add_Category.objects.create(category=category)
                cat=add_Category.objects.all()
                return render(request,'admin/addedcategory.html',{'cat': cat})
                
        else:
            cat=add_Category.objects.all()
            return render(request,'admin/addedcategory.html',{'cat': cat})
    else:
        return redirect(adlogin)

def catdiscount(request,id1):   
    if request.method == 'POST':
        percen = request.POST['percent']
        product = add_Category.objects.filter(id=id1).update(discount=percen)
        return redirect(addedcategory)

def deletediscount(request,id1):
    product = add_Category.objects.filter(id=id1).update(discount=0)
    return redirect(addedcategory)
     

def delcategory(request,pk):
    if request.session.has_key('key'):
        pro = add_Category.objects.get(id=pk)
        pro.delete()
        return redirect(addedcategory) 
    else:
        return redirect(adlogin)

def orderlist(request):
    order = Order.objects.all()
    return render(request,'admin/orderlist.html',{'order':order})

def orderchange(request):
    if request.method == 'POST':
        values =request.POST['Value']
        id1 = request.POST['id1']
        print(values)
        print(id1)
        orders = Order.objects.get(id=id1)
        orders.Status = values
        orders.save()
        return JsonResponse('true',safe=False)
    else:
        return redirect(orderlist)


def reporttable(request):
    if request.method =='POST':
        date1=request.POST['date1']
        date2=request.POST['date2'] 
        print(date1)
        ordertable = Order.objects.filter(Date__range=[date1,date2]) 
        return render(request,'admin/reporttable.html',{'ordertable':ordertable})  
    else:
        ordertable = Order.objects.all()
        return render(request,'admin/reporttable.html',{'ordertable':ordertable})

def viewcoupon(request):
    if request.method=="POST":
          coupon_code=request.POST['coupon_code']
          offer=request.POST['offer_percentage']
          Coupon=Coupons.objects.create(Coupon_code=coupon_code,Offer=offer)
          Coupon.save()
    coupon_get=Coupons.objects.all()
    return render(request,'admin/viewcoupons.html',{'coupon':coupon_get})

def delete_coupon(request,pk):
    if request.session.has_key('key'):
        coupon = Coupons.objects.get(id=pk)
        coupon.delete()
        return redirect(viewcoupon) 
    else:
        return redirect(adlogin)   




def adlogout(request):
    request.session.flush()
    return redirect(adlogin)