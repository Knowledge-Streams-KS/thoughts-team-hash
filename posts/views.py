from django.shortcuts import render, get_object_or_404, redirect
from .forms import form_for_thoughts, CommentForm, PostShareForm
from .models import Post, Comment
from django.http import JsonResponse , HttpResponse
from users.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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





def view_posts_all(request, user_id):
    user = User.objects.get(id = user_id)
    post = Post.objects.all(user =user)
    return HttpResponse(post)

#Creating Comments!
#@csrf_exempt
#@login_required  
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
            form = CommentForm()
            return render(request, "posts/comment_form.html", {"post": post, "comment_form": form})
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

            comment = Comment(user=request.user, post=post, text=text)
            comment.save()
            
            return HttpResponse("Comment Successfully by.")
        else:
            return render(request, "posts/comment_form.html", {"post": post, "comment_form": form})

    return HttpResponse("Invalid request method.")

#Retreive Comment
def retrieve_comments(request, id):
        
    post = Post.objects.get(id=id)   
    comments = Comment.objects.filter(post=post)   
    comment_data = []

    for comment in comments:
        comment_info = {
            "Comment_text": comment.text,
            "User": comment.user.username,
        }
        comment_data.append(comment_info)

    return JsonResponse(comment_data, safe=False)

#Update Comment

def update_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user 
    comment = Comment.objects.filter(post=post, user=user).first()

    if request.method == "GET":
        if comment:  
            form = CommentForm(initial={'text': comment.text})
        else:
            form = CommentForm()
        return render(request, "posts/comment_update_form.html", {"post": post, "comment_form": form, "comment":comment})

    if request.method == "POST":
        if comment: 
            form = CommentForm(request.POST)
        else:
            form = CommentForm(request.POST)
        
        if form.is_valid():
            if not comment:
                comment = Comment(user=user, post=post)
            comment.text = form.cleaned_data["text"]
            comment.save()
            return HttpResponse("Comment successfully updated.")
        else:
            return render(request, "posts/comment_update_form.html", {"post": post, "comment_form": form, "comment":comment})

    return HttpResponse("Invalid request method.")

# Delete Comment
def delete_comment(request, post_id, comment_id):
    
    post = get_object_or_404(Post, id=post_id)
    
    comment = get_object_or_404(Comment, id=comment_id, post=post)

    if request.user == comment.user:
        comment.delete()
        return HttpResponse("Comment successfully deleted.")
    else:
        return HttpResponse("You do not have permission to delete this comment.")

#Sharing Posts*******************
def sharePost(request):
    if request.method == "GET":
        form = PostShareForm()
        return render(request,"posts/post_share.html",{"form":form})
    
    if request.method =="POST":
        form = PostShareForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_id = form.cleaned_data['user_id']
            
            post = Post.objects.get(name=name)
            user = get_object_or_404(User, pk=user_id)

            all_posts = user.shared_posts.all()
            if post in all_posts:
                return HttpResponse(f'Post {post.name} already shared')
            else:
                share = user.shared_posts.add(post)
                return HttpResponse(f"Post {post.name} shared Successfully.")
        else:    
            return render(request,"posts/post_share.html",{"form":form})

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


