from django.shortcuts import render, get_object_or_404, redirect
from .forms import form_for_thoughts, CommentForm
from .models import Post, Comment
from django.http import JsonResponse , HttpResponse
from users.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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

#Creating Comments!
#@csrf_exempt
@login_required  
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
            form = CommentForm(request.POST, instance=comment)
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
