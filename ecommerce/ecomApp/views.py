from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.decorators import login_required
from ecomApp.models import category,usermember,product,cart1

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def admin_home(request):
    return render(request,'admin/admin_home.html')

@login_required(login_url='login')
def user_home(request):

    usr = usermember.objects.get(user= request.user)
    return render(request,'user/user_home.html',{ 'user1': usr })

@login_required(login_url='login')
def add_category(request):

    if request.method == "POST":
        catg  = request.POST.get('categ')
        c1 = category(cat_name = catg)
        c1.save()
        return redirect('/add_category')

    return render(request,'admin/addcategory.html')

@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        fkey = request.POST['cat']
        cat_id = category.objects.get(id = fkey)
        if request.FILES.get('file') is not None:
           pic=  request.FILES.get('file')
        else:
           pic = ''
        prod = product(
                    prod_name = request.POST['product'],
                    description = request.POST['desc'],
                    price = request.POST['price'],
                    category = cat_id,
                    image = pic
        )
        prod.save()
    categories = category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request,'admin/addproduct.html',context)

@login_required(login_url='login')
def show_prod(request):
    prod = product.objects.all()
    return render(request,'admin/showproduct.html' ,{ 'product' : prod })

@login_required(login_url='login')
def del_prod(request,pk):
    
    prod = product.objects.get(id=pk)
    prod.delete()
    return redirect('show_prod')


def all_prod(request):

    usr = usermember.objects.get(user= request.user)
    prod = product.objects.all()
    context = { 'product' : prod ,
                'user1' : usr}
    return render(request,'user/allprod.html' ,context )


def women(request):

    usr = usermember.objects.get(user= request.user)
    prod = product.objects.filter(category_id=7)
    context = { 'product' : prod ,
                'user1' : usr}
    return render(request,'user/women.html' ,context)

def men(request):
    
    usr = usermember.objects.get(user= request.user)
    prod = product.objects.filter(category_id=8)
    context = { 'product' : prod ,
                'user1' : usr}

    return render(request,'user/men.html' ,context)

def kids(request):

    usr = usermember.objects.get(user= request.user)
    prod = product.objects.filter(category_id=9)
    context = { 'product' : prod ,
                'user1' : usr}

    return render(request,'user/kids.html' ,context)


@login_required(login_url='login')
def add_cart(request,pk):
    prod = product.objects.get(id = pk)
    usr = User.objects.get(id = request.user.id)
    enter = cart1(product = prod, user = usr)
    enter.save()
    return redirect('cart')

@login_required(login_url='login')
def cart(request):
    if request.user is not None:
        usr = usermember.objects.get(user= request.user)
        prod = cart1.objects.filter(user = request.user)
        context = { 'product' : prod ,
                    'user1' : usr}
        return render(request,'user/cart.html',context)
    

@login_required(login_url='login')
def del_cart(request,pk):
    prod = cart1.objects.get(id = pk)
    prod.delete()
    return redirect('cart')


@login_required(login_url='login')
def show_user(request):
    member = usermember.objects.all()
    return render(request,'admin/showuser.html' ,{ 'member' : member })

@login_required(login_url='login')
def edit_user(request):
    user = User.objects.get(id=request.user.id)
    user1 = usermember.objects.get(user=request.user)

    if request.method == "POST":
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.username=request.POST['uname']
        #password=request.POST['pswd']
        #cpassword=request.POST['cpswd']
        user.email=request.POST['email']
        user1.address = request.POST['address']
        user1.c_num = request.POST['c_num']
        if len(request.FILES)!=0 :
            user1.profile_pic = request.FILES.get('file')
                
        user.save()
        user1.save()

    context={
        'user1' : user1
    }
    return render(request,'user/edit_prof.html', context)


@login_required(login_url='login')
def del_user(request,pk):
    
    usr = usermember.objects.get(id=pk)
    user = User.objects.get(id=usr.user_id)
    usr.delete()
    user.delete()
    return redirect('show_user')


def usercreate(request):
    
    if request.method=='POST':

        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['pswd']
        cpassword=request.POST['cpswd']
        email=request.POST['email']
        address = request.POST['address']
        c_num = request.POST['c_num']
        if request.FILES.get('file') is not None:
           pic=  request.FILES.get('file')
        
            
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('/usercreate')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                u = User.objects.get(id = user.id)
                
                um = usermember(
                    address = address,
                    c_num = c_num,
                    user = u,
                    profile_pic = pic
                    )
                um.save()
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('/usercreate')   
        return redirect('/usercreate')

    return render(request,'signup.html')


        

def login(request):
        
    if request.method == 'POST':
        
        username = request.POST['uname']
        password = request.POST['pswd']
        user = auth.authenticate(username= username,password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('admin_home')
            else:
                
                auth.login(request,user)
                messages.info(request,f'Welcome {capfirst(username)}')
                return redirect('user_home')
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('/login')
    
    return render(request,'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')
