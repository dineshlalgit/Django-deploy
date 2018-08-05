from django.shortcuts import render
from userauth.forms import UserForm,UserprofileinfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"userauth/index.html")


@login_required
def log_out(request):
    logout(request)

    return render(request,"userauth/index.html")



def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form =UserprofileinfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                print("found it")

                profile.profile_pics = request.FILES['profile_pics']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form =UserprofileinfoForm()

    return render(request,"userauth/register.html",{'registered':registered,'profile_form':profile_form,'user_form':user_form})

def  user_login(request):
   
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('passwd')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

                return render(request,"userauth/index.html")

            else:
                return HttpResponse("Your not logged in")
        
        else:
            print("invalid details provided")
            print("username {} and password {}".format(username,password))

    else:
        return render(request,"userauth/login.html",{})