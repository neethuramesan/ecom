from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from app1.models import Category,Product,Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
import os

# Create your views here.
def index(request):
    return render(request,'home.html')
def loginn(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def adminhome(request):
    return render(request,'adminhome.html')

def login1(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pas = request.POST['password']
        usr = auth.authenticate(username=uname,password=pas) 
        if usr is not None:
            if usr.is_superuser:
                login(request,usr)
                messages.info(request,f'Welcome Admin : {uname}')
                return redirect('adminhome')
            else:
                login(request,usr)
                messages.info(request,f'Welcome  {uname}')
                return redirect('/')
def signupaction(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pas = request.POST['pass']
        cpas = request.POST['cpass']
        email = request.POST['email']
        addrss = request.POST['address']
        contact = request.POST['contact']
        photo = request.FILES['image']
 

        if pas == cpas :
            if User.objects.filter(username = uname).exists():
                messages.info(request,'username exists')
                return redirect('signup')
            else:
                usr = User.objects.create_user(first_name = fname, last_name = lname, password = pas,email=email,username=uname)
                usr.save()
                b = Customer(user=usr,address = addrss,contactnumber=contact,image=photo)
                b.save()
                return redirect('home')
        else:
            messages.info(request,'password doesnt match')
            return redirect('signup') 