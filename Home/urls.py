from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login_user,name='login_user'),
    path('logout',views.logout_user,name='logout_user'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name="profile"),
    path('dweet',views.dweet,name="dweet"),
    path('followers',views.followers,name="followers"),
    path('following',views.following,name="following"),
    path('suggestions',views.suggestions,name="suggestions"),
    path('user/<slug:username>',views.user_profile,name="user_profile"),
    path('unfollow/<slug:username>',views.unfollow,name="unfollow"),
    path('test',views.test),
]
