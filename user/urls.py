from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.index,name='index'),
     path('signup/',views.signup,name='signup'),
     path('Referals/<int:id>/',views.Referals,name='Referals'),
     path('referalsignup/',views.referalsignup,name='referalsignup'),
     path('login/',views.login,name='login'),
     path('profile/',views.profile,name='profile'),
     path('search/',views.search,name='search'),
     path('editprofile/',views.editprofile,name='editprofile'),
     path('updateprofile/',views.updateprofile,name='updateprofile'),
     path('addressedit/<int:id1>/',views.addressedit,name='addressedit'),
     path('deleteaddress/<int:id1>/',views.deleteaddress,name='deleteaddress'),
     path('statuschange/',views.statuschange,name='statuschange'),
     path('orderschoose/<int:id1>/',views.orderschoose,name='orderschoose'),
     path('changepassword/',views.changepassword,name='changepassword'),
     path('otp_starter/',views.otp_starter,name='otp_starter'),
     path('otp_finish/',views.otp_finish,name='otp_finish'),
     path('logout/',views.logout,name='logout'),
     path('shopage/<int:pk>/',views.shopage,name='shopage'),
     path('cart_delete/<int:id>/',views.cart_delete,name='cart_delete'),
     path('procart/',views.procart,name='procart'),
     path('addtocart/<int:pk>/',views.addtocart,name='addtocart'),
     path('updatecart/',views.updatecart,name='updatecart'),
     path('refcoupon/',views.refcoupon,name='refcoupon'),
     path('checkout/',views.checkout,name='checkout'),
     path('chooseaddress/<int:id>',views.chooseaddress,name='chooseaddress'),
     path('payment/',views.payment,name='payment'),
     path('cod/',views.cod,name='cod'),
     path('befpaypal/',views.befpaypal,name='befpaypal'),
     path('paypal/',views.paypal,name='paypal'),
     path('paypal_confirm/',views.paypal_confirm,name='paypal_confirm'),
     path('razarpay/',views.razarpay,name='razarpay'),
     path('razar_success/',views.razar_success,name='razar_success'),
     path('ordersuccess/',views.ordersuccess,name='ordersuccess')

     


]
