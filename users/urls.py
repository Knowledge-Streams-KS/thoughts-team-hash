from django.contrib import admin
from django.urls import path
from .views import *
from . import views


urlpatterns = [
     path('signup/', views.user_signup_form),
     path('loginin/', views.user_signin_form),
     # path('index/', views.homeview),
     path('getuser/<id>/',views.get_user),
     path('deluseruser/<id>/',views.delete_user),
     path('edit/<id>/',views.update_user),

     
     # path('post/',views.post_thoughts),
     # path("user/<pk>/", UserDetailView.as_view(), name="user-detail"),

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
