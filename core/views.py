from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .models import *
from .forms import UserPostForm


def view_post_detail(request,id):
    print(id)
    post = Post.objects.get(id=id)
    context ={
        'post':post
    }
    return render(request,'post_detail.html',context)



def view_post(request):
    print(request.GET)
    search_query = request.GET.get('query')
    if search_query is not None and search_query !="":
        # yedi search_query pass bhako xa ra khali chaina bhane filter garnu paryo
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        # natra sabai post select garnu paryo
        posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request,'view_post.html',context)


def profile(request,userid): 
    user = User.objects.get(id = userid)
    photos = Photos.objects.filter(user = user)
    context = { 
               'photos':photos
               }
    return render(request,'profile.html',context)


def view_profile(request,username):

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse('User with provided username does not exist')

    posts = user.posts.all()  # reverse relationship with related_name
    print(posts)
    context = {
        'user':user,
        'posts':posts
    }

    return render(request,'profile_page.html',context)

def post_view(request):


    if not request.user.is_authenticated:
        # if not logged in
        return HttpResponse("Please Login to Post")   
    

    form = UserPostForm()

   
    
    if request.method == 'POST':
        form = UserPostForm(request.POST,request.FILES)
        if form.is_valid():
            post_object = form.save(commit=False)
            post_object.user = request.user
            post_object.save()
            # post_obj = form.save(commit=False) # doesn't save in database
            # post_obj.user = request.user
            # post_obj.save()
            return redirect('/view_profile/')
    


    context = {
        'form':form
    }


    return render(request,'post.html',context)
