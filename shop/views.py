from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages
from django.http import HttpResponse
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
from django.http import JsonResponse

# Methods
def home(request):
    product=Products.objects.filter(trending=1) #Condition for checking the trending the latest product
    return render(request,"shop/index.html",{"product":product})#It will shows an trending products below the home pages! 

def thank_page(request):
    return render(request,"shop/thank.html") 


def fav_page(request):
    if request.headers.get("x-requested-with")=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=Products.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status':'Product is Already in Favourite'},status=200)
                else:
                    Favourite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product added Favourite'},status=200)
        else:
            return JsonResponse({'status':'Login to Add Favroute'},status=200)
    else: 
            return JsonResponse({'status':'Invalid Access'},status=200)


def add_to_cart(request):
    if request.headers.get("x-requested-with")=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            # print(data['product_qty'])
            # print(data['pid'])
            # print(request.user.id)
            product_qty=data['product_qty']
            product_id=data['pid']
            product_status=Products.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status':'Product is Already in Cart'},status=200)
                else:
                    if product_status.quantity>product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product added Successfully'},status=200)
                    else:
                        return JsonResponse({'status':'Product  Stock Not Available!'},status=200)
        else:
            return JsonResponse({'status':'Login to Add Cart'},status=200)
    else:
            return JsonResponse({'status':'Invalid Access'},status=200)



def logout_page(request):
    if request.user.is_authenticated:#Checking out the user got first loged in with inbuild fun
        logout(request)#It is also an inbuild fun it will be used to logout the user
        messages.success(request,"Logout successfully!!")#msg will be displayed
    return redirect("/")#its get redirected to the home page


def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        messages.success(request,"Login to View Cart!!")
        return redirect("/")

def fav_viewpage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{"fav":fav})
    else:
        messages.success(request,"Login to Add Favourite!!")
        return redirect("/")


def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")


def remove_fav(request,fid):
    Favitem=Favourite.objects.get(id=fid)
    Favitem.delete()
    return redirect("/fav_viewpage")



def login_page(request):#Once the user get logined means the it can allowed again 
    if request.user.is_authenticated:#its an condition for checking the user got login or not
        return redirect("/")#its get redirected to the home page
    else:
        if request.method=='POST':#Lets check that user requesting method is poost or not 
            name=request.POST.get('username')#If the request is post means it will get an input and save it the name and component name is "username"
            pwd=request.POST.get('password')#If the request is post means it will get an input and save it the pwd
            user=authenticate(request,username=name,password=pwd)#create an variable called user then via build in method pass the name to "username" and pwd to "password" finally it assign to the that variable user
            if user is not None:# it will checks an user is empty or not
                login(request,user)#Then login is inbulid fun it will login the user by creating the seesion
                messages.success(request,"Loged in Successfully!!")#just for msg
                return redirect("/")#After the login it will redirect to Home page
            else:
                messages.error(request,"Invalid Username and Password!!!")#else part
        return render(request,"shop/login.html")#It shows an login page



def regis(request):
    form=CustomUserForm()#To call the fun
    if request.method=='POST': #To get an Action
        form=CustomUserForm(request.POST) #To validate an Form
        if form.is_valid(): #Checking the Form
            form.save() #It get Success means save the forms otherwise defaultly it will shows an error Message
            messages.success(request,"Registration Successfull You Can Login Now!!") #It will throw an Success Message
            return redirect('/login')#It will redirected the login the page after the register
    return render(request,"shop/register.html",{"form":form}) #Form for Submiting 
# For collecting the collection pages


def collect(request):
    category=Catagory.objects.filter(status=0)
    return render(request,'shop/collection.html',{"category":category})
# For collecting the inner images 


def collections(request,fname):
    if(Catagory.objects.filter(fname=fname,status=0)):
        product=Products.objects.filter(catagory__fname=fname)
        return render(request,'shop/products/index.html',{"product":product,"category_name":fname})
    else:
        messages.warning("No Such Product found in this Category!!")
        return redirect('collection')
    
# def product_details(request,cname,pname):
#     # return HttpResponse("Product Details")
#     # It will be redirected to the main same page because of not building the path of that exact product
#     return redirect('collect')

def product_details(request,cname,pname):#Ar first it will be get an three parameter names
    if(Catagory.objects.filter(fname=cname,status=0)):#Then it will check status is 0 or  not
        if(Products.objects.filter(fname=pname,status=0)):#Similarly in the product_list also
            products=Products.objects.filter(fname=pname,status=0).first()#Then create the variable products and finds that product in products calss in form of object the filter the productname when the status is zero
            #It will takes an first product and render to the particular html page
            return render(request,'shop/products/product_detail.html',{"product":products})#Then it will renter the request to the corresponding page
        else:
            messages.warning("No Such Product found!!!") # It will be redirected to the main same page because of not building the path of that exact product
            return redirect('collection')
    else:
        messages.warning("No Such Category found !!!") # It will be redirected to the main same page because of not building the path of that exact product
        return redirect('collection')