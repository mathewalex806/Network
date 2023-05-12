from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.http import JsonResponse

from .models import User, Post, Like

def index(request):
    post = Post.objects.all()
    posts = post.order_by("-timestamp").all()
    paginator = Paginator(posts, 8) # Show 8 posts per page.
    page_number = 1
    if request.method =="POST":
        page_number_next = request.POST['page']
        if page_number_next == "Next":
            page_number += 1
        if page_number_next == "Previous":
            page_number = 1
    
    allLikes = Like.objects.all()
    whoYouLiked = []
    try:
        for i in allLikes:
            if i.user == request.user:
                whoYouLiked.append(i.post.id)
    except:
        pass



    page_obj = paginator.get_page(page_number)
    query= page_obj.object_list
    return render(request, 'network/index.html', { "posts" : query,  "whoYouLiked": whoYouLiked})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pic = request.POST["imgurl"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, pic=pic)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new_post(request):
    if request.method == "POST":
        title_inp= request.POST["title"]
        content = request.POST["description"]
        post = Post( title= title_inp ,description=content, user=request.user)
        post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/new_post.html")
    
def profile(request, username):
    user = User.objects.get(username= username)
    post = Post.objects.filter(user = User.objects.get(username = username))
    posts = post.order_by("-timestamp").all()
    no = len(posts)
    follow = user.followers.all()
    a=[]
    for i in follow:
        a.append(i.username)
    return render(request, "network/profile.html", {"user_obj": user, "posts": posts, "no": no, "follow": a})

def following(request):
    user = User.objects.get(username = request.user.username)
    following_users = user.following.all()
    posts = Post.objects.filter(user__in = following_users).order_by("-timestamp").all()
    following_no = len(posts)
    return render(request, "network/following.html", {"posts": posts, "no": following_no, 'following_users': following_users})

def follow_unfollow(request):
    if request.method == "POST":
        action = request.POST["follow"]
        if action == 'unfollow':
            username = request.POST["username"]
            user = User.objects.get(username = username)
            request.user.following.remove(user)
            return HttpResponseRedirect(reverse("profile", args=(username,)))
        if action == 'follow':
            username = request.POST["username"]
            user = User.objects.get(username = username)
            request.user.following.add(user)
            return HttpResponseRedirect(reverse("profile", args=(username,)))
    else:
        return HttpResponseRedirect(reverse("index"))
    
def edit(request, post_id):
    if request.method == "POST":
        data = json.loads(request.body)
        edit_post = Post.objects.get(id = post_id)
        edit_post.description = data["description"]
        edit_post.save()
        return JsonResponse({"message": "Post edited successfully."}, status=201)

def remove_like(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id = post_id)
        user  = User.objects.get(username = request.user.username)
        like  = Like.objects.filter(user = user, post = post)
        like.delete()
        return JsonResponse({"message": "Like removed successfully."}, status=201)
    
def add_like(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id = post_id)
        user  = User.objects.get(username = request.user.username)
        like = Like(user = user, post = post)
        like.save()
        return JsonResponse({"message": "Like added successfully."}, status=201)
