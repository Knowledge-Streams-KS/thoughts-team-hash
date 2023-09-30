from django.shortcuts import render , HttpResponse
from .forms import User_Signup_form, User_Signin_form
from .models import User

# Create your views here.

def user_signup_form(request):
    if request.method == "GET":
        form = User_Signup_form()
        
        return render(request,"users/signup_and_signin.html",{"signup":form})

    if request.method == "POST":
        form = User_Signup_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password= form.cleaned_data["password"]
            email= form.cleaned_data["email"]
            phone_number= form.cleaned_data["phone_number"]

            user = User( username = username, email = email, phone_number = phone_number,first_name = first_name, last_name = last_name)
            user.set_password(password)
            user.save()
    
            
    else:
        return render(request,"users/signup_and_signin.html",{"signup":form})
    
    return HttpResponse("User Created Done")


def user_signin_form(request):
    if request.method == "GET":
        form = User_Signin_form()
        
        return render(request,"users/signup_and_signin.html",{"signin":form})

    if request.method == "POST":
        form = User_Signin_form(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password= form.cleaned_data["password"]

            user = User( username = username )
            user.check_password(password)
        
    
            
    else:
        return render(request,"users/signup_and_signin.html",{"signin":form})
    
    return HttpResponse("User Created Done")