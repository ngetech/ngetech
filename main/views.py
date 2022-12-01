from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            response = HttpResponseRedirect(reverse("main:home"))
            response.set_cookie('last_login',str(datetime.datetime.now()))
            return response
        else:
            messages.info(request,'Username atau Password salah')
    context = {'login_form':LoginForm()}
    return render(request,'login.html',context)

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        is_user_already_exist = User.objects.filter(username=username).exists()
        if password_1 == password_2 and not is_user_already_exist:
            user = User.objects.create_user(username=username,password=password_2)
            if user is not None:
                user.save()
                return redirect('main:login')
            else:
                messages.info(request,'Ops! something went wrong')
        elif password_1 != password_2:
            messages.info(request,'Password doesnt match')
        elif is_user_already_exist:
            messages.info(request,'User already exist')
        else:
            messages.info(request,'Ops! something went wrong')
    form = {'register_form':RegisterForm()}
    return render(request,'register.html',form)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:home'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def flutter_login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({
              "status": True,
              "username": request.user.username,
              "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": f"Failed to Login as {username}, check your email/password."
        }, status=401)

@csrf_exempt
def flutter_register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_user_already_exist = User.objects.filter(username=username).exists();
        if not is_user_already_exist:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return JsonResponse({
                "status": True,
                "username": user.username,
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to register, username already exist."
            }, status=401)
    else:
        return JsonResponse({
            "status": "error"
        }, status=401)

@csrf_exempt
def flutter_logout_user(request):
    try:
        logout(request)
        return JsonResponse({
            "status": True,
            "message": "Successfully Logged out!"
        }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)
