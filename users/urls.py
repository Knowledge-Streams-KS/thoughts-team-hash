from django.contrib import admin
from django.urls import path
from .views import *
from . import views


urlpatterns = [
    
     # path('signup/', views.user_signup_form),
     path("create/user/", UserCreateView.as_view(), name="create-user"),
     path('getuser/<int:pk>/', login_required(UserDisplayView.as_view()), name = 'get_user'),
     path('deleteuser/<int:pk>/',login_required(UserDeleteView.as_view())),
     path('edit/<pk>/',login_required(UserUpdateView.as_view()), name = 'edit'),

     path('home/', views.index , name = 'index'),

     path('loginin/', views.user_signin_form , name = 'create-user'),
     path('logout/', views.logout_view , name = 'logout-user'),


     path("user/profile/", login_required(ProfileCreateView.as_view()), name="create-profile"),
     path('get/profile/<int:pk>/', login_required(ProfileDisplayView.as_view()), name = 'get_user_profile'),
     path('delete/user-profile/<int:pk>/',login_required(ProfileDeleteView.as_view())),
     path('edit/profile/<pk>/',login_required(ProfileUpdateView.as_view()), name = 'edit-profile'),



     
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
