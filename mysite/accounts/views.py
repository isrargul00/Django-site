from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect("records:home")
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, 'logedin')
            return redirect('records:home')
        else:
            messages.add_message(request,messages.WARNING,'Your data is wrong')
            return redirect('accounts:login')

        pass
    else:
        return render(request,'accounts/login.html')

@login_required()
def user_logout(request):
    messages.add_message(request, messages.INFO, 'Logout')
    logout(request)
    return redirect("accounts:login")

def registration(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        email    =  request.POST.get('email')
        password =  request.POST.get('password')
        print(f'--------------------{username}---------------')
        obj = User.objects.create_user(username=username,email=email,password=password)
        print(f'----------------come form user data {obj}---------')
        obj.save()
        messages.add_message(request,messages.SUCCESS,'your is sucess full create')
        return redirect('accounts:login')
    else:
        return render(request,'accounts/registration.html')