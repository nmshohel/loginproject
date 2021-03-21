from django.shortcuts import render,redirect
from loginprojectapp.forms import UserForm,UserInfoForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.urls import reverse

def index(request):
    context={}
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_basic_info=User.objects.get(pk=user_id)
        user_more_info=UserInfo.objects.get(user__pk=user_id)
        context={'user_basic_info':user_basic_info,'user_more_info':user_more_info}
    return render(request,'loginprojectapp/index.html',context)
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        user_info_form=UserInfoForm(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            user_info=user_info_form.save(commit=False)
            user_info.user=user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic=request.FILES['profile_pic']

            user_info.save()
            registered=True

    else:
        user_form=UserForm()
        user_info_form=UserInfoForm()

    context={'user_form':user_form,'user_info_form':user_info_form,'registered':registered}
    return render(request, 'loginprojectapp/register.html',context)
def user_profile(request):
    user_profile=User.objects.get(username='nur')
    user_info_profile=UserInfo.objects.get(user=2)
    context={'user_profile':user_profile,'user_info_profile':user_info_profile}
    print(User.username)
    return render(request, 'loginprojectapp/user_profile.html',context)


def user_login(request):
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        user_pass=request.POST.get('password')
        print(user_name)
        print(user_pass)
        user=authenticate(username=user_name, password=user_pass)
        if user:
            login(request, user)
            return redirect('index')


    # context={}
    return render(request, 'loginprojectapp/user_login.html')
