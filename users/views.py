from django.shortcuts import render , HttpResponse,redirect
from .forms import User_Signin_form
from .models import User
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout






# Create your views here.
class UserCreateView(CreateView):
    model = User
    fields = ["username", "email","password","phone_number","first_name","last_name"]
    success_url = "/users/getuser/{id}"    
    template_name = "users/user_form.html"
    
    


class UserDisplayView(DetailView):
        model = User
        template_name = "users/profile_form.html"

# from .forms import ProfileUpdateForm
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ["phone_number"]
#     success_url = "/loginin/" 
#     # form_class = ProfileUpdateForm  
#     # template_name= "users/profile_update.html"
# from .forms import UserUpdateForm
class UserUpdateView(UpdateView):
    model = User
    fields = ['phone_number']
    # form_class = UserUpdateForm
    # template_name = "users/profile_update.html"
    success_url = "/loginin/"
    # def get_success_url(self):
    #     return reverse('get_user', kwargs={'pk': self.object.id})


class UserDeleteView(DeleteView):
     model = User
     success_url = "users/deactivate.html"

    

def user_signin_form(request):

    if request.method == "GET":
        signin = User_Signin_form()
        
        return render(request,"users/login.html",{"signin":signin})



    if request.method == "POST":
    
        signin = User_Signin_form(request.POST)
        if signin.is_valid():
             username = signin.cleaned_data["username"]
             password= signin.cleaned_data["password"]
       
    else:
            return render(request,"users/login.html",{"signin":signin })
            

    return login_user(request,username,password)


def login_user(request,username,password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        user_name = User.objects.get( username = user.username)
        return redirect(f"/users/getuser/{request.id}")
    else:
        return HttpResponse("Not valid")
      


# def logout_view(request):
#     logout(request)
#     success_url = "/users/loginin/"


def post_thoughts(request):
         return render(request,"users/post_form.html")



# def get_user(request , pk):
#         user  = User.objects.get(pk = pk)
#         return render(request,"users/user_detail.html",{"user":user})
      

def delete_user(request , id):
        user  = User.objects.get(pk = id)
        user.delete()
        return render(request,"users/deactivate.html")
      



from .models import UserProfile

class ProfileCreateView(CreateView):
    model = UserProfile
    fields = ["bio","city","dob"]
    template_name = "users/profile/userprofile_form.html"
    success_url = "/"

class ProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ["bio","city","dob"]
    success_url = "/users/get/profile/{id}"    
    template_name= "users/profile/profile_update.html"

    # def get_object(self,queryset = None):
    #       return UserProfile.objects.get(user__username=self.request.user.username)
    


class ProfileDeleteView(DeleteView):
     model = UserProfile
     template_name= "users/profile/userprofile_confirm_delete.html"
    #  success_url = "users/deactivate.html"

    
class ProfileDisplayView(DetailView):
        model = UserProfile
        template_name = "users/profile/profile_detail.html"


# def update_user(request, id):
#         user = get_object_or_404(User, id=id)
#         if request.method == "GET":
#             form = User_Signup_form(instance = user)        
#             return render(request,"users/user_detail.html",{"signup":form})

#         if request.method == "POST":
#                 form = User_Signup_form(request.POST)
#                 if form.is_valid():
#                     username = form.cleaned_data["username"]
#                     first_name = form.cleaned_data["first_name"]
#                     last_name = form.cleaned_data["last_name"]
#                     # password= form.cleaned_data["password"]
#                     email= form.cleaned_data["email"]
#                     phone_number= form.cleaned_data["phone_number"]
#                     # user = User( username = username, email = email, phone_number = phone_number,first_name = first_name, last_name = last_name)
#                     # user.set_password(password)
#                     # user.save()
#                     user.username = username    
#                     user.first_name = first_name
#                     user.last_name = last_name
#                     # user.set_password(password)
#                     user.email= email
#                     user.phone_number = phone_number
#                     user.save()
#                 else:
#                         return render(request,"users/user_detail.html",{"signup":form })
                
               
#         else:
#             return render(request,"users/user_detail.html",{"signup":form })
    
#         return HttpResponse("Done")


