from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.
def register(request):
    form=RegisterForm(request.POST or None)
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid(): # forms.py deki clean funksiyasini caqirmaq ucun
            username=form.cleaned_data.get("username") # values={"username": username, "password": password,"confirm": confirm} ("username") valuesde yazilan key olan "username" dir
            password=form.cleaned_data.get("password")

            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.info(request, 'Basariyla kayit oldunuz')
            return redirect("index")
    context={
        "form":form
    }
    return render(request,"register.html",context)
    """if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid(): # forms.py deki clean funksiyasini caqirmaq ucun
            username=form.cleaned_data.get("username") # values={"username": username, "password": password,"confirm": confirm} ("username") valuesde yazilan key olan "username" dir
            password=form.cleaned_data.get("password")

            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)

            return redirect("index")
        context={
            "form":form
        }
        return render(request,"register.html",context)
        
    else:
        form=RegisterForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)"""
def loginUser(request):
    form = LoginForm(request.POST or None)
    context={
        "form":form
    }
    if request.method=="POST":
        if form.is_valid(): #clean metodu cagrilir
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            user=authenticate(username=username,password=password)

            if user is None:
                messages.info(request,"Kullanici adi ve ya parola Hatali")
                return render(request,"login.html",context)

            messages.success(request,"Basariyla Giris Yapildi")
            login(request,user)
            return redirect("index")
   
    return render(request,"login.html",context)
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Basariyla Cikis Yaptiniz")
    return redirect("index")
    