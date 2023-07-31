from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from store.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
import json
from django.http import JsonResponse






# Create your views here.
def home(request):
    return render(request,"page/index.html")

def about(request):
    template=loader.get_template('page/about.html')
    return HttpResponse(template.render())

def shop(request):
    shop=cycles.objects.all()
    template=loader.get_template('page/shop.html')
    return render(request,"page/shop.html",{"cycless":shop})

def product_details(request,pname):
      if(cycles.objects.filter(name=pname,status=0)):
        products=cycles.objects.filter(name=pname,status=0).first()
        return render(request,"page/product_details.html",{"cycless":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return redirect('shop')

def contact(request):
    template=loader.get_template('page/contact.html')
    return HttpResponse(template.render())

def comunication(request):
    if request.method=="POST":
        name=request.POST['Name']
        mail=request.POST['Mail']
        contact=request.POST['Contact']
        select=request.POST['Select']
        message=request.POST['Textarea']

        obj=contacted()
        obj.Name=name
        obj.Mail=mail
        obj.Contact=contact
        obj.Select=select
        obj.Message=message
        obj.save()

        mydata=contacted.objects.all()
        return redirect('contact')
    return render(request,'page/contact.html')


def childs(request):
    childs=cycles.objects.all()
    template=loader.get_template('page/child.html')
    return render(request,"page/child.html",{"cycless":childs})

def men(request):
    products=cycles.objects.all()
    template=loader.get_template('page/men.html')
    return render(request,"page/men.html",{"cycless":products})

def women(request):
    womens=cycles.objects.all()
    template=loader.get_template('page/women.html')
    return render(request,"page/women.html",{"cycless":womens})

def adventures(request):
    adver=cycles.objects.all()
    template=loader.get_template('page/adventures.html')
    return render(request,"page/adventures.html",{"cycless":adver})





def order(request):
     if request.method=="POST":
         sku=request.POST['sku']
         name=request.POST['name']
         number=request.POST['number']
         if number=='':
             number=None
         door=request.POST['door']
         address=request.POST['address']
         city=request.POST['city']

         obj=buy()
         obj.Sku=sku
         obj.Name=name
         obj.Number=number
         obj.Door=door
         obj.Address=address
         obj.City=city 
         obj.save()

         mydata=buy.objects.all()
         return redirect('shop')

     return render(request,'page/buys.html')

def buys(request,bname):
  
    if(cycles.objects.filter(name=bname,status=0)):
        buyed=cycles.objects.filter(name=bname,status=0).first()
        return render(request,"page/buys.html",{"cycless":buyed})
    else:
        return redirect('buys')

      

def cart_page(request):
    if request.user.is_authenticated:
       cart=Cart.objects.filter(user=request.user)
       return render(request,"page/cart.html",{"Carts":cart})
    else:
     return redirect("/")

def add_to_cart(request):
      if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
          data=json.load(request)
          product_qty=data['product_qty']
          product_id=data['pid']
          #print(request.user.id)
          product_status=cycles.objects.get(id=product_id)
          if product_status:
              if Cart.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'Product Already in Cart'}, status=200)
              else:
                if product_status.quantity>=product_qty:
                  Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                  return JsonResponse({'status':'Product Added to Cart'}, status=200)
                else:
                  return JsonResponse({'status':'Product Stock Not Available'}, status=200)
          else:
            return JsonResponse({'status':'Login to Add Cart'}, status=200)
        else:
          return JsonResponse({'status':'Invalid Access'}, status=200)

 


def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")


def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("login")
    return render(request,"login.html")      

def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("cart_page")



def register(request):
    form=CustomUserForm()
    if request.method=='POST':
       form=CustomUserForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,"Registaton is success you login now..!")
          return redirect('login')
    return render(request,"register.html",{'form':form})


