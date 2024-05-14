from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('',views.index,name='index'),
 path('login1',views.login1,name='login1'),
  path('signup',views.signup,name='signup'),
 path('loginn',views.loginn,name='loginn'),
path('adminhome',views.adminhome,name='adminhome')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)