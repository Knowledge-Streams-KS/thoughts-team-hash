from django.shortcuts import render
from .forms import form_for_thoughts
from .models import Post
from django.http import JsonResponse , HttpResponse
from users.models import User
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.


def createform_html(request , id):
    if request.method == "GET":
        form = form_for_thoughts()
        return render(request,"posts/post_form.html",{"form":form})

    if request.method == "POST":
        form = form_for_thoughts(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            file = form.cleaned_data["file"]
            person = User.objects.get(id = id)
            post = Post(user = person, name = name, content = content, media = file)
            post.save()
        else:
            return render(request,"posts/post_form.html",{"form":form})
    
    return HttpResponse("done")




def view_posts_all(request, user_id):
    user = User.objects.get(id = user_id)
    post = Post.objects.all(user =user)
    return HttpResponse(post)


