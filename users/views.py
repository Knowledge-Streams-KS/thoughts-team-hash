from django.shortcuts import render , HttpResponse
from .forms import User_Signup_form, User_Signin_form
from .models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404



# Create your views here.

def user_signup_form(request):
    if request.method == "GET":
        form = User_Signup_form()        
        signin = User_Signin_form()
        return render(request,"users/signup_and_signin.html",{"signup":form,"signin":signin})

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
                        return render(request,"users/signup_and_signin.html",{"signup":form })
                
               
    else:
        return render(request,"/signup_and_signin.html",{"signup":form })
    
    return HttpResponse("Done")

# def homeview(request):
#      return render(request,"users/index.html")

def user_signin_form(request):

    if request.method == "GET":
        signin = User_Signin_form()
        
        return render(request,"users/signup_and_signin.html",{"signin":signin})



    if request.method == "POST":
    
        signin = User_Signin_form(request.POST)
        if signin.is_valid():
            usern = signin.cleaned_data["username"]
            passw = signin.cleaned_data["password"]
                    
            user = authenticate(request, username=usern, password=passw)
            user.check_password(passw)
            if user is not None:
                        login(request, user)
                        return HttpResponse("login success")
            else:
                        return HttpResponse("Not valid")
    else:
            return render(request,"users/signup_and_signin.html",{"signin":signin })
            

    return HttpResponse("Logged in")


def post_thoughts(request):
         return render(request,"users/post_form.html")



def get_user(request , id):
        user  = User.objects.get(pk = id)
        return render(request,"users/user_detail.html",{"user":user})
      

def delete_user(request , id):
        user  = User.objects.get(pk = id)
        user.delete()
        return render(request,"users/deactivate.html")
      



def update_user(request, id):
        user = get_object_or_404(User, id=id)
        if request.method == "GET":
            form = User_Signup_form()        
            return render(request,"users/user_detail.html",{"signup":form})

        if request.method == "POST":
                form = User_Signup_form(request.POST)
                if form.is_valid():
                    username = form.cleaned_data["username"]
                    first_name = form.cleaned_data["first_name"]
                    last_name = form.cleaned_data["last_name"]
                    password= form.cleaned_data["password"]
                    email= form.cleaned_data["email"]
                    phone_number= form.cleaned_data["phone_number"]
                    # user = User( username = username, email = email, phone_number = phone_number,first_name = first_name, last_name = last_name)
                    # user.set_password(password)
                    # user.save()
                    user.username = username    
                    user.first_name = first_name
                    user.last_name = last_name
                    user.set_password(password)
                    user.email= email
                    user.phone_number = phone_number
                else:
                        return render(request,"users/user_detail.html",{"signup":form })
                
               
        else:
            return render(request,"users/user_detail.html",{"signup":form })
    
        return HttpResponse("Done")


