from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Profile,Dweet,UserFollowing
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import datetime
import random
from django.contrib import messages


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        current_user = request.user
        current_profile = Profile.objects.get(user=current_user)
        
        #dweet list had all the dweets by dweet_authors
        dweets_list = []
        
        # dweet_authors has the all the user present in following along with current user
        dweet_authors = []

        # To get all the following users
        following = current_user.followers.all()
        for f in following:
            dweet_authors.append(f.user_id)
        dweet_authors.append(request.user)
        
        #To get all the dweets by the dweet_authors
        for author in dweet_authors:
            dweets_by_author = author.Author.all()
            for _ in dweets_by_author:
                dweets_list.append(_)
        
        # Remove These Comments
        # print(f'These are the authors of the feed list {dweet_authors}')
        # print(f"These are the dweets by authors {dweets_list}")
        # print("The Feed dweet:")

        # These are the dweets
        # for dweet in dweets_list:
        #     print(f'Dweet:{dweet.dweet}')
        #     print(f'Time:{dweet.time}')

        suggestions = random.sample(list(Profile.objects.all()),3)
        context={
            "user_name":current_user.username,
            "user_followers":len(current_user.following.all()),
            "user_following":len(current_user.followers.all()),
            "user_bio":current_profile.bio,
            "dweets":dweets_list,
            "suggestions": suggestions,
            "len_dweets":len(dweets_list),
        }

        return render(request,'home.html',context)
    else:
        return render(request,"index.html")

def login_user(request):

    # POST
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid User")
            return redirect('/login')
    
    # GET
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'index.html')

def logout_user(request):
    logout(request)
    return redirect("/")
    
def register(request):
    #POST
    if request.method == "POST":
        username = request.POST["name_r"]
        pwd = request.POST["password_r"]

        # Fix RE-ENTER PASSWORD
        # rpwd = request.POST["repassword"]
        
        bio = request.POST["bio"]
        user = User.objects.create_user(username=username,password=pwd)
        user.save()
        profl = Profile(user = user,bio=bio)
        profl.save()
        return redirect("/")
    
    #GET
    # return render(request,'register.html')


def dweet(request):
    # POST
    if request.method == "POST":
        dweet = request.POST["dweet"]
        user_id = request.user
        time = datetime.datetime.now()+datetime.timedelta(hours=5.5)
        dwt = Dweet(dweet=dweet,user_id = user_id,time = time)
        dwt.save() #This creates a New Dweet
        return redirect("/")
    
    # GET
    return render(request,"dweet.html")


# User Profile
def user_profile(request,username):
    user_at_link = User.objects.get(username=username)
    user_at_link_profile = Profile.objects.get(user=user_at_link)

    # print(f'This is the username at this link: {username}')
    
    own_profile_status = True
    if user_at_link== request.user :
        own_profile_status = True
        # print("Same USer hes looking at his own profile")
    else:
        own_profile_status = False
        # print("Different User")

    #POST
    if request.method=="POST":
        usr_f = UserFollowing(user_id=user_at_link,following_user_id=request.user)
        usr_f.save()
        
        # Need to Fix This
        # - Update Followers Count
        # - Update Following Count
        return redirect("/")

    #GET
    # Final Code for returning the followers and follwing users
    user = user_at_link
    follower = user.following.all()
    following = user.followers.all()
    # print(f"{len(following)} Following :")
    # for i in following:
    #     print(i.user_id)
    # print(f"{len(follower)} Followers :")
    # for j in follower:
    #     print(j.following_user_id)

    f_status = True
    if UserFollowing.objects.filter(user_id = user_at_link,following_user_id=request.user).exists():
        f_status = True
    else:
        f_status = False

    # if UserFollowing(user_id=user_at_link,following_user_id=request.user).exist()

    context={
        "user_name":user_at_link.username,
        "user_followers":len(follower),
        "user_following":len(following),
        "user_bio":user_at_link_profile.bio,
        "dweets":Dweet.objects.filter(user_id = user),
        "len_dweets":len(Dweet.objects.filter(user_id = user)),
        "own_profile_status":own_profile_status,
        "follow_unfollow":f_status,
    }
    return render(request,"profile.html",context)


# This is test endpoint
def test(request):
    # All Fine Guess So...
    # This "user" is the user who's details we are requesting
    user = request.user
    y = user.following.all()
    x = user.followers.all()
    print("Following :")
    for i in x:
        print(i.user_id)
    print("Followers :")
    for j in y:
        print(j.following_user_id)
    return render(request,"dwitter_home.html")
    # return HttpResponse("OK")
    # return render(request,"suggestions.html")


def suggestions(request):
    current_user = request.user
    current_profile = Profile.objects.get(user=current_user)
    context={
        "user_name":current_user.username,
        "user_followers":len(current_user.following.all()),
        "user_following":len(current_user.followers.all()),
        "user_bio":current_profile.bio,
        "users":Profile.objects.all(),
    }
    return render(request,"suggestions.html",context)


def following(request):
    current_user = request.user
    current_profile = Profile.objects.get(user=current_user)
    context={
        "user_name":current_user.username,
        "user_followers":len(current_user.following.all()),
        "user_following":len(current_user.followers.all()),
        "user_bio":current_profile.bio,
        "following":current_user.followers.all(),
    }
    return render(request,"following.html",context)

def followers(request):
    current_user = request.user
    current_profile = Profile.objects.get(user=current_user)
    context={
        "user_name":current_user.username,
        "user_followers":len(current_user.following.all()),
        "user_following":len(current_user.followers.all()),
        "user_bio":current_profile.bio,
        "followers":current_user.following.all(),
    }
    return render(request,"followers.html",context)

def profile(request):
    return redirect(f"user/{request.user}")

def unfollow(request,username):
    user_at_link = User.objects.get(username=username)
    UserFollowing.objects.filter(user_id=user_at_link,following_user_id=request.user).delete()
    return redirect("/")