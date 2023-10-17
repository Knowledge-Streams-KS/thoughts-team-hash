from django.contrib import admin
from django.urls import path
from .views import *
from django.views.generic.edit import CreateView

from . import views


urlpatterns = [
     # path('create-post/<id>', views.createform_html),
     # path('view-posts/<id>/', views.view_posts_all),
     path('view/all/posts/',login_required(PostDisplayView.as_view()), name = 'all-product'),   #login setup requried 
     path('createThought/', login_required(CreateThought.as_view()), name='CreateThought'),
     path('updateThought/<int:pk>/', login_required(UpdateThought.as_view()), name= 'UpdateThought'),
     path('deleteThought/<int:pk>/',login_required(DeleteThought.as_view()), name='deleteThought'),
     path('detailThought/<int:pk>', login_required(PostThought.as_view()), name="detailThought"),
    #  path('update-tweet/', views.update_tweet),
    #  path('created/',views.createform_html),
    #  path('shared_with/',views.shared_with),
    #  path('comment/',views.comment_form),

    #  path("listview/", TweetListView.as_view(), name="tweet-list"),
    #  path("tweet/<pk>/", TweetDetailView.as_view(), name="tweet-detail"),
    #  path("tweetcreate/", TweetCreateView.as_view(), name="tweet-create"),
    #  path("about/", AboutView.as_view()),

     # path('done/',views.createform_html),

#Comments
     path('add_comment/<int:id>/', views.add_comment, name='add_comment'),
     path('retrieve_comments/<int:id>/', views.retrieve_comments, name='retrieve_comments'),
     # path('update_comment/<int:post_id>/', views.update_comment, name='update_comment'),
path('update_comment/<int:post_id>/<int:comment_id>', views.update_comment, name='update_comment'),

     path('delete_comment/<int:post_id>/<int:comment_id>/', views.delete_comment, name='delete_comment'),

path('display_posts/', views.display_posts, name='display_posts'),

#SharePosts
     path('sharePost/<int:pk>', views.sharePost, name='sharePost'),
     path('shared_withme/',login_required(SharedWithMe.as_view())),
]
