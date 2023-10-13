from typing import Any
from django.db import models
from django.shortcuts import render
from .forms import form_for_thoughts
from .models import Post
from django.http import JsonResponse , HttpResponse
from users.models import User
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Post



# Create your views here.


# def createform_html(request , id):
#     if request.method == "GET":
#         form = form_for_thoughts()
#         return render(request,"posts/post_form.html",{"form":form})

#     if request.method == "POST":
#         form = form_for_thoughts(request.POST,request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             content = form.cleaned_data["content"]
#             file = form.cleaned_data["file"]
#             person = User.objects.get(id = id)
#             post = Post(user = person, name = name, content = content, media = file)
#             post.save()
#         else:
#             return render(request,"posts/post_form.html",{"form":form})
    
#     return HttpResponse("done")




# def view_posts_all(request, user_id):
#     user = User.objects.get(id = user_id)
#     post = Post.objects.all(user =user)
#     return HttpResponse(post)
from django.urls import reverse

class PostCreateView(CreateView):
    model = Post
    fields = ['user','name', 'content']
    template_name="posts/post_form.html"
    success_url = "/posts/view/all/posts/"



class PostUpdateView(UpdateView):
    model = Post
    fields = ['name', 'content']
    # template_name_suffix = "/post_list.html"
    success_url = "/posts/view/all/posts/"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/posts/view/all/posts/"
    template_name = "posts/post_list.html"


    # class PostDetailView(DetailView):
    #     model = Post
    #     template_name = '/posts/posts_list.html'


from django.views.generic.list import ListView

class PostDisplayView(ListView):
        model = Post
        success_url="/view/all/posts/"
        template_name = '/posts/post_list.html'

        def get_queryset(self):
             user = User.objects.get(id = 3)
             posts = Post.objects.filter(user = user)
             return posts
        

class PostDetailView(DetailView):
    # specify the model to use
    model = Post
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_pk = self.kwargs.get('pk')
    #     # Access the pk of the user or perform any additional logic
    #     context['user_pk'] = user_pk
    #     return context

