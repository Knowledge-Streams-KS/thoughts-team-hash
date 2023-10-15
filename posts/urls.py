from django.contrib import admin
from django.urls import path
from .views import *
from . import views


urlpatterns = [
     path('create-post/<id>', views.createform_html, name ='create-post'),
     path('view-posts/<id>/', views.view_posts_all),
    #  path('delete-tweet/', views.delete_tweet),
    #  path('update-tweet/', views.update_tweet),
    #  path('created/',views.createform_html),
    #  path('shared_with/',views.shared_with),
    #  path('comment/',views.comment_form),

    #  path("listview/", TweetListView.as_view(), name="tweet-list"),
    #  path("tweet/<pk>/", TweetDetailView.as_view(), name="tweet-detail"),
    #  path("tweetcreate/", TweetCreateView.as_view(), name="tweet-create"),
    #  path("about/", AboutView.as_view()),

     # path('done/',views.createform_html),



]
