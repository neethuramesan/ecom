from django.urls import path
from . import views

urlpatterns = [
   
   path('',views.home,name='home'),
   path('admin_home',views.admin_home,name='admin_home'),
   path('login',views.login,name='login'),
   path('user_home',views.user_home,name='user_home'),
   path('usercreate', views.usercreate,name='usercreate'),
   path('cart', views.cart,name='cart'),
   path('logout',views.logout,name='logout'),
   path('show_user',views.show_user,name='show_user'),
   path('del_user/<pk>',views.del_user,name='del_user'),
   path('add_category',views.add_category,name = 'add_category'),
   path('add_product',views.add_product,name = 'add_product'),
   path('show_prod',views.show_prod,name='show_prod'),
   path('del_prod/<pk>',views.del_prod,name='del_prod'),
   path('all_prod',views.all_prod,name='all_prod'),
   path('add_cart/<pk>',views.add_cart,name='add_cart'),
   path('del_cart/<pk>',views.del_cart,name='del_cart'),
   path('edit_user',views.edit_user,name='edit_user'),
   path('women' , views.women,name='women'),
   path('men' , views.men,name='men'),
   path('kids' , views.kids,name='kids'),

]