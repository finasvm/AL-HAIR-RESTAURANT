from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse 
from django.contrib.auth.models import User,auth
from .models import *
from admin1.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.hashers import check_password
import random
from twilio.rest import Client
import string   


# Create your views here.

def index(request):
   
    # if request.user.is_active == False:
    #     auth.logout(request)
    #     return render(request,'user/index.html',{'prod':prod})
    if request.user.is_authenticated and request.user.is_active == True:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        cart_user = Person.objects.get(user=request.user)
        cart_obj = Cart.objects.filter(user=cart_user)
        procat = {'prod':prod,'cat': cat,'cartcount':cart_obj}
        return render(request,'user/index1.html',procat)
    
    else:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        procat = {'prod':prod,'cat': cat}
        return render(request,'user/index1.html',procat)
    
def signup(request):
    prod = addProduct.objects.all()
    cat = add_Category.objects.all()
    procat = {'prod':prod,'cat': cat}

    if request.user.is_authenticated:
        return redirect(index)
    else:  
        if request.method =='POST' :
            username=request.POST['username']
            email=request.POST['email']
            number=request.POST['number']
            password=request.POST['password']
            password_confirm=request.POST['password_confirm'] 
            if password == password_confirm:
                if User.objects.filter(username=username).exists():
                    return JsonResponse('false3', safe=False) 
                elif User.objects.filter(email=email).exists():
                    return JsonResponse('false4', safe=False)
                elif Person.objects.filter(number=number).exists():
                    return JsonResponse('false5', safe=False)
                else:
                    u = User.objects.create_user(username=username,email=email,password=password)
                    Person.objects.create(user=u,number=number)
                    return JsonResponse('true', safe=False) 
                
            else:
                return JsonResponse('false', safe=False)
        else:
            return render(request,'user/register1.html',procat)


def Referals(request,id):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        procat = {'prod':prod,'cat': cat}
        request.session['referalid']=id 
        return render(request,'user/referalsignup.html',procat)

def referalsignup(request):
    if request.user.is_authenticated:
            return redirect(index)
    else:
        if request.method =='POST' :
            username=request.POST['username']
            email=request.POST['email']
            number=request.POST['number']
            password=request.POST['password']
            password_confirm=request.POST['password_confirm'] 
            if password == password_confirm:
                if User.objects.filter(username=username).exists():
                    return JsonResponse('false3', safe=False) 
                elif User.objects.filter(email=email).exists():
                    return JsonResponse('false4', safe=False)
                elif Person.objects.filter(number=number).exists():
                    return JsonResponse('false5', safe=False)
                else:
                    u = User.objects.create_user(username=username,email=email,password=password)
                    p = Person.objects.create(user=u,number=number) 
                    ref_code1 = random.randint(10000000,9999999999)
                    user_refer = Person.objects.get(user=u)
                    Referal.objects.create(refCoupon_code=ref_code1,referaluser=user_refer)
                    ref_code2 = random.randint(100000000,9999999999999)
                    ref_user = request.session['referalid']
                    refff = User.objects.get(id=ref_user)
                    reee = Person.objects.get(user=refff)
                    referal_givenuser = Referal.objects.create(refCoupon_code=ref_code2,referaluser=reee)
                    del  request.session['referalid']
                    return JsonResponse('true', safe=False) 
                
            else:
                return JsonResponse('false', safe=False)
        else:
            prod = addProduct.objects.all()
            cat = add_Category.objects.all()
            procat = {'prod':prod,'cat': cat}
            return render(request,'user/referalsignup.html',procat)

   


def login(request):
    prod = addProduct.objects.all()
    cat = add_Category.objects.all()
    procat = {'prod':prod,'cat': cat}
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method =='POST':
            username=request.POST['username']
            password=request.POST['password']
            # user = auth.authenticate(username=username,password=password)
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.is_active==True:
                    user = auth.authenticate(username=username,password=password)
                    if user is not None:
                        auth.login(request,user)
                        return JsonResponse('true', safe=False)
                        #return redirect('welcome')
                    else:
                        return JsonResponse('false', safe=False)
                        #messages.info(request,'USERNAME AND PASSWORD IS WRONG')
                else:
                    return JsonResponse('block',safe=False)
            else:
                return JsonResponse('false',safe=False)
        else:
            return render(request,'user/register1.html',procat)

def profile(request):
    if request.user.is_authenticated:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        cart_user = Person.objects.get(user=request.user)
        cart_obj = Cart.objects.filter(user=cart_user)
        user_details = Person.objects.get(user=request.user) 
        address_details = Address.objects.filter(user=user_details.id)
        order_details = Order.objects.filter(user_order=user_details.id)
        ref = Person.objects.get(user=request.user)
        if Referal.objects.filter(referaluser=ref).exists():
            Ref = Referal.objects.filter(referaluser=ref)
        else:
            Ref = str(0)
        context = {'user_details':user_details,'address_details':address_details,'order_details':order_details,'prod':prod,'cat': cat,'cartcount':cart_obj,'Ref':Ref}
        return render(request,'user/profile.html',context)
    else:   
        return redirect(index)
def changepassword(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            oldpass = request.POST['oldpass']
            newpass1 = request.POST['newpass']
            conpass = request.POST['conpass']
            current_password = request.user.password
            matchcheck = check_password(oldpass,current_password)
            if matchcheck == True:
                if newpass1 == conpass:
                    u = User.objects.get(id=request.user.id)
                    u.set_password(newpass1)
                    u.save()
                    return JsonResponse('true',safe=False)
                else:
                    return JsonResponse('false',safe=False)
            else:
                return JsonResponse('false1',safe=False)
    else:
        return redirect(index)

def editprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username1 = request.POST['username1']
            number1 = request.POST['number1']
            email1= request.POST['email1']
            if User.objects.filter(username=username1).exclude(id=request.user.id).exists():
                return JsonResponse('false3', safe=False) 
            elif User.objects.filter(email=email1).exclude(id=request.user.id).exists():
                return JsonResponse('false4', safe=False)
            elif Person.objects.filter(number=number1).exclude(user=request.user).exists():
                return JsonResponse('false5', safe=False)
            else:
                u = User.objects.filter(id=request.user.id).update(username=username1,email=email1)
                Person.objects.filter(user=request.user).update(user=u,number=number1)
                return JsonResponse('true',safe=False)
        else:
            return redirect(profile)
    else:
        return redirect(index)

def addressedit(request,id1):
    if request.user.is_authenticated:
        if request.method == "POST":
            fullname = request.POST['fullname']
            pincode = request.POST['pincode']
            city = request.POST['city']
            state = request.POST['state']
            housename = request.POST['housename']
            landmark = request.POST['landmark']
            Address.objects.filter(id=id1).update(Full_name=fullname,pinCode=pincode,city=city,state=state,HouseName=housename,landMark=landmark)
            return redirect(profile)
        else:
            return redirect(profile)
    else:
        return redirect(index)
def deleteaddress(request,id1):
    if request.user.is_authenticated:
        car = Address.objects.get(id=id1)
        car.delete()
        return redirect(profile)
    else:
        return redirect(index)

def statuschange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            values =request.POST['Value']
            id1 = request.POST['id1']
            orders = Order.objects.get(id=id1)
            orders.Status = values
            orders.save()
            return JsonResponse('true',safe=False)
        else:
            return redirect(profile)
    else:
        return redirect(index)

def orderschoose(request,id1):
    if request.user.is_authenticated:
        product = addProduct.objects.filter(id=id1)
        return render(request,'user/orderchoose.html',{'prod':product})
    else:
        return redirect(index)



@csrf_exempt
def updateprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fileName=request.FILES.get('image_upload')
            person = Person.objects.get(user=request.user)
            person.prof_Image = fileName    
            person.save()
            return JsonResponse('true',safe=False)
    else:
        return redirect(index)
def otp_starter(request):
    if request.user.is_authenticated:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        cart_user = Person.objects.get(user=request.user)
        cart_obj = Cart.objects.filter(user=cart_user)
        procat = {'prod':prod,'cat': cat,'cartcount':cart_obj}
        if request.method == 'POST':
            number1 = request.POST['number_user']
            if Person.objects.filter(number=number1).exists():
                request.session['phone'] = number1
                global otp
                otp = random.randint(1000,9999)
                account_sid = 'ACe9dc627b24bcaaf909d52a0485457588'
                auth_token = 'bfb0d094200ed46fea63bfc61644a277'
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    body= f"Your otp is {otp}",
                    from_='+13133074664',
                    to=f'+917510968482'
                    )
                return JsonResponse('true',safe=False)
            else:
                return JsonResponse('false',safe=False) 
        else:
            return render(request,'user/otp_starter.html'.procat)
    else:
        return redirect(index)
def otp_finish(request):
    prod = addProduct.objects.all()
    cat = add_Category.objects.all()
    cart_user = Person.objects.get(user=request.user)
    cart_obj = Cart.objects.filter(user=cart_user)
    procat = {'prod':prod,'cat': cat,'cartcount':cart_obj}
    if request.method == 'POST':
        otp_num = request.POST['otp_number']
        number1 = request.session['phone'] 
        myuser = Person.objects.get(number=number1)
        user2 = User.objects.get(id=myuser.user.id)
        global otp
        if otp == int(otp_num):
            auth.login(request,user2)
            return JsonResponse('true',safe=False)
        else:
            return JsonResponse('false',safe=False)
    else:
        return render(request,'user/otp_finisher.html',procat)

def search(request):
    if request.user.is_authenticated:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        cart_user = Person.objects.get(user=request.user)
        cart_obj = Cart.objects.filter(user=cart_user)
        if request.method == 'GET':
            search1 = request.GET['search']
            product = addProduct.objects.filter(p_name__icontains=search1)
            procat = {'prod':prod,'cat': cat,'cartcount':cart_obj,'prod':product}
            return render(request,'user/search.html',procat)
        else:
            procat = {'prod':prod,'cat': cat,'cartcount':cart_obj,'prod':product}
            return render(request,'user/search.html',procat)
    else:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        if request.method == 'GET':
            search1 = request.GET['search']
            product = addProduct.objects.filter(p_name__icontains=search1)
            procat = {'prod':prod,'cat': cat,'prod':product}
            return render(request,'user/search.html',procat)



        
def shopage(request,pk):
    if request.user.is_authenticated:
        product = add_Category.objects.get(id=pk)
        product_cat = addProduct.objects.filter(p_cate=product.id)
        cat = add_Category.objects.all()
        cart_user = Person.objects.get(user=request.user)
        cart_obj = Cart.objects.filter(user=cart_user)    
        return render(request,'user/filterpro.html',{'categ': product_cat , 'cat':cat,'cartcount':cart_obj })
    else:
        product = add_Category.objects.get(id=pk)
        product_cat = addProduct.objects.filter(p_cate=product.id)
        cat = add_Category.objects.all()
        return render(request,'user/filterpro.html',{'categ': product_cat , 'cat':cat})


def procart(request):
    if request.user.is_authenticated:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        cart_user = Person.objects.get(user=request.user)
        cart_obj = Cart.objects.filter(user=cart_user)
        user1 = Person.objects.get(user=request.user)
        user_cart = Cart.objects.filter(user=user1)
        sub_total = 0
        grand_total = 0
        total_price=0
        for car in user_cart:
            if (car.products.p_cate.discount == 0):
                total_price = (car.count) * (car.products.p_price)
                car.total_price=total_price    
                sub_total = sub_total + total_price
                grand_total = sub_total
            else:
                total_price = (car.count) * (car.products.discountprice)
                car.total_price=total_price    
                sub_total = sub_total + total_price
                grand_total = sub_total
        context = {'proda':user_cart,'prod':prod,'cat':cat,'cartcount':cart_obj,'sub_total':sub_total,'grand_total':grand_total}
        return render(request,'user/cart1.html',context) 
    else:
        return redirect(login)

   
def addtocart(request,pk):
    if request.user.is_authenticated:
        prod = addProduct.objects.all()
        cat = add_Category.objects.all()
        cart_user = Person.objects.get(user=request.user)
        cart_obj = Cart.objects.filter(user=cart_user)    
        cart = addProduct.objects.get(id=pk)
        uuser = request.user
        user = Person.objects.get(user=uuser.id)
        Mycart, created  = Cart.objects.get_or_create(user=user,products=cart)
        Mycart.count += 1 
        Mycart.save()
        return render(request,'user/index1.html',{'prod':prod,'cat':cat,'cartcount':cart_obj})
    else:
        return redirect(login)
@csrf_exempt
def cart_delete(request,id):   
    car = Cart.objects.get(id=id)
    car.delete()
    return JsonResponse('true',safe=False)

@csrf_exempt
def updatecart(request):
    if request.method == 'POST':
        cartid = request.POST['cartid']
        qty = request.POST['qty']
        persuser = Person.objects.get(user=request.user)
        cart = Cart.objects.get(id=cartid)
        cart.user = persuser
        cart.count = qty 
        cart.save()

        return redirect(procart)


def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Fullname = request.POST['fullname']
            pincode = request.POST['pincode']
            city = request.POST['city']
            state = request.POST['state']
            housename = request.POST['housename']
            landmark = request.POST['landmark']
            user = Person.objects.get(user=request.user)
            address = Address.objects.create(Full_name=Fullname,pinCode=pincode,city=city,state=state,HouseName=housename,landMark=landmark,
            user=user)  
            user1 = Person.objects.get(user=request.user) 
            user_cart = Cart.objects.filter(user=user1)
            sub_total = 0
            grand_total = 0
            total_price=0
            for car in user_cart:
                if (car.products.p_cate.discount == 0):
                    total_price = (car.count) * (car.products.p_price)
                    sub_total = sub_total + total_price
                    grand_total = sub_total
                else:
                    total_price = (car.count) * (car.products.discountprice)
                    car.total_price=total_price    
                    sub_total = sub_total + total_price
                    grand_total = sub_total
            user = Person.objects.get(user=request.user)
            address_unique = Address.objects.filter(user=user)
            return render(request,'user/checkout.html',{'address':address_unique,'grand_total':grand_total})    
        else:
            user1 = Person.objects.get(user=request.user)
            user_cart = Cart.objects.filter(user=user1)
            sub_total = 0
            grand_total = 0
            total_price=0
            for car in user_cart:
                if (car.products.p_cate.discount == 0):
                    total_price = (car.count) * (car.products.p_price)
                    sub_total = sub_total + total_price
                    grand_total = sub_total
                else:
                    total_price = (car.count) * (car.products.discountprice)
                    car.total_price=total_price    
                    sub_total = sub_total + total_price
                    grand_total = sub_total
            user = Person.objects.get(user=request.user)
            address_unique = Address.objects.filter(user=user)
            return render(request,'user/checkout.html',{'address':address_unique,'grand_total':grand_total})
    else:
        return redirect(login)

def refcoupon(request):
    user1 = Person.objects.get(user=request.user)
    user_cart = Cart.objects.filter(user=user1)
    sub_total = 0
    grand_total = 0
    total_price=0
    for car in user_cart:
        quantity = car.count
        if (car.products.p_cate.discount == 0):
            price = car.products.p_price
        else:
            price = car.products.discountprice
        total_price = quantity * price
        sub_total = sub_total + total_price
        grand_total1 = sub_total
    if request.method == 'POST':
        Coupon_typed = request.POST['code']
        if Referal.objects.filter(refCoupon_code=Coupon_typed):
            request.session['refcoupon'] = Coupon_typed
            grand_totals = (grand_total1-((grand_total1/100)*10))
        elif Coupons.objects.filter(Coupon_code=Coupon_typed):
            request.session['refcoupon'] = Coupon_typed
            coup = Coupons.objects.get(Coupon_code=Coupon_typed)
            grand_totals = (grand_total1-(grand_total1/100)*coup.Offer)
            coup.Status= False
            coup.save()
        else:
            grand_totals = grand_total1
        user = Person.objects.get(user=request.user)
        address_unique = Address.objects.filter(user=user)
        return render(request,'user/checkout.html',{'address':address_unique,'grand_total':grand_totals})
    else:
        user = Person.objects.get(user=request.user)
        address_unique = Address.objects.filter(user=user)
        return render(request,'user/checkout.html',{'address':address_unique,'grand_total':grand_total1})


@csrf_exempt
def chooseaddress(request,id):
    request.session['addressid']=id
    return JsonResponse('true',safe=False)



@csrf_exempt
def payment(request):
    if request.method == 'POST':
        value = request.POST['value']
        if value == 'razarpay':
            return JsonResponse('true',safe=False)
        elif value == 'paypal':
            return JsonResponse('true1',safe=False)
        elif value == 'cod':
            return JsonResponse('true2',safe=False)
    else:
        return redirect(checkout)

def cod(request):
    if request.user.is_authenticated:
        user = Person.objects.get(user=request.user)
        try:
             address = request.session['addressid']
        except:
            messages.info(request,'Please select the address')
            return redirect(checkout)
        address1 = Address.objects.get(id=address)
        cart = Cart.objects.filter(user=user)
        for car in cart:
            if (car.products.p_cate.discount == 0):
                Order.objects.create(user_order=user,Product=car.products,address=address1,Qty=car.count,Price=car.count*car.products.p_price,Status="ordered",PaymentMethod="COD")
                car.delete()
            else:
                Order.objects.create(user_order=user,Product=car.products,address=address1,Qty=car.count,Price=car.count*car.products.discountprice,Status="ordered",PaymentMethod="COD")
                car.delete()

        return redirect(ordersuccess)
    else:
        return redirect(login)

def befpaypal(request):
    user1 = Person.objects.get(user=request.user)
    user_cart = Cart.objects.filter(user=user1)
    sub_total = 0
    grand_total = 0
    total_price=0
    for car in user_cart:
        quantity = car.count
        if (car.products.p_cate.discount == 0):
            price = car.products.p_price
        else:
            price = car.products.discountprice
        total_price = quantity * price
        sub_total = sub_total + total_price
        grand_total = sub_total
    grand_total=grand_total
    if request.session.has_key('refcoupon'):
        reference =  request.session['refcoupon']
        if Referal.objects.filter(refCoupon_code = reference):
            grand_total = (grand_total-((grand_total/100)*10))
            grand_total = int(grand_total/72)
        elif Coupons.objects.filter(Coupon_code=reference):
            coup = Coupons.objects.get(Coupon_code=reference)
            grand_total = (grand_total -(grand_total/100)*coup.Offer)
            grand_total = int(grand_total/72)
    else:
        grand_total = int(grand_total/72)
    context = {'grand_total':grand_total}
    return render(request,'user/paypal.html',context)

def paypal(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return JsonResponse('true',safe=False)
    else:
        return redirect(login)


def paypal_confirm(request):
    if request.user.is_authenticated:
        user = Person.objects.get(user=request.user)
        try:
            address = request.session['addressid']
        except:
            messages.info(request,'Please select the address')
            return redirect(checkout)
        address = request.session['addressid']
        address1 = Address.objects.get(id=address)
        cart = Cart.objects.filter(user=user)
        for car in cart:
            if (car.products.p_cate.discount == 0):
                Order.objects.create(user_order=user,Product=car.products,address=address1,Qty=car.count,Price=car.count*car.products.p_price,Status="ordered",PaymentMethod="PAYPAL")
                car.delete()
            else:
                Order.objects.create(user_order=user,Product=car.products,address=address1,Qty=car.count,Price=car.count*car.products.discountprice,Status="ordered",PaymentMethod="PAYPAL")
                car.delete()

        return redirect(ordersuccess)
    else:
        return redirect(login)


def razarpay(request):
    user1 = Person.objects.get(user=request.user)
    user_cart = Cart.objects.filter(user=user1)
    sub_total = 0
    grand_total = 0
    total_price=0
    for car in user_cart:
        quantity = car.count
        if (car.products.p_cate.discount == 0):
            price = car.products.p_price
        else:
            price = car.products.discountprice
        total_price = quantity * price
        sub_total = sub_total + total_price
        grand_total = sub_total
    if request.session.has_key('refcoupon'):
        reference =  request.session['refcoupon']
        if Referal.objects.filter(refCoupon_code = reference):
            grand_total = (grand_total-((grand_total/100)*10))
        elif Coupons.objects.filter(Coupon_code=reference):
            coup = Coupons.objects.get(Coupon_code=reference)
            grand_total = (grand_total -(grand_total/100)*coup.Offer)
    else:
        grand_total = grand_total
    context = {'grand_total':grand_total}
    return render(request,'user/razarpay.html',context)

@csrf_exempt
def razar_success(request):
    if request.user.is_authenticated:
        user = Person.objects.get(user=request.user)
        try:
            address = request.session['addressid']
        except:
            messages.info(request,'Please select the address')
            return redirect(checkout)
        address = request.session['addressid']
        address1 = Address.objects.get(id=address)
        cart = Cart.objects.filter(user=user)
        for car in cart:
            if (car.products.p_cate.discount == 0):
                Order.objects.create(user_order=user,Product=car.products,address=address1,Qty=car.count,Price=car.count*car.products.p_price,Status="ordered",PaymentMethod="PAYPAL")
                car.delete()
            else:
                Order.objects.create(user_order=user,Product=car.products,address=address1,Qty=car.count,Price=car.count*car.products.discountprice,Status="ordered",PaymentMethod="PAYPAL")
                car.delete()
        return redirect(ordersuccess)
    else:
        return redirect(login)

def ordersuccess(request):
    if request.user.is_authenticated:
        if request.session.has_key('refcoupon'):           
            reference =  request.session['refcoupon']    
            if Referal.objects.filter(refCoupon_code = reference):
                Ref = Referal.objects.get(refCoupon_code = reference)
                Ref.delete()
                del request.session['refcoupon']
                return render(request,'user/ordersuccess.html')
            else:
                return render(request,'user/ordersuccess.html')
        else:
            return render(request,'user/ordersuccess.html')
             
    else:
         return redirect(index)



    

   
def logout(request):
    auth.logout(request)
    return redirect(index)