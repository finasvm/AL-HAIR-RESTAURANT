from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adlogin,name="adlogin"),
    path('adpanel/',views.adpanel,name="adpanel"),
    path('usertable/',views.usertable,name='usertable'),
    path('block/<int:pk>/',views.block,name='block'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('deletepro/<int:pk>/',views.deletepro,name='deletepro'),
    path('editpro/<int:pk>/',views.editpro,name='editpro'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('catdiscount/<int:id1>/',views.catdiscount,name='catdiscount'),
    path('deletediscount/<int:id1>/',views.deletediscount,name='deletediscount'),
    path('delcategory/<int:pk>/',views.delcategory,name='delcategory'),
    path('addedcategory/',views.addedcategory,name='addedcategory'),
    path('toadd/',views.toadd,name='toadd'),
    path('orderlist/',views.orderlist,name='orderlist'),
    path('orderchange/',views.orderchange,name='orderchange'),
    path('reporttable/',views.reporttable,name='reporttable'),
    path('viewcoupon/',views.viewcoupon,name='viewcoupon'),
    path('delete_coupon/<int:pk>/',views.delete_coupon,name='delete_coupon'),
    path('adlogout/',views.adlogout,name='adlogout')

]
