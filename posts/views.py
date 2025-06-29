from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    
    return render(request, 'posts.html', {'posts': posts})


@login_required
def addpost(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        
        posts = Post(title=title, body=description, author=request.user)
        posts.save()
        
        return redirect('/')

    
    return render(request, 'addpost.html')

@login_required
def update(request, pk):

    post = get_object_or_404(Post, id=pk, author=request.user)
    
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        post.title = title
        post.body = description
        post.save()

        return redirect('/')
     
    return render(request, 'update.html', {'post': post})





@login_required
def delete(request, pk):
    posts = get_object_or_404(Post, id=pk, author=request.user)
    posts.delete()
    
    return redirect('/')


def search(request):

    query=request.GET['query']
    posts = Post.objects.filter(title__icontains=query)
    
    return render(request, 'search.html',{'posts': posts})


def signup(request):
    if request.method=='POST':
        email = request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('/')

        user=User.objects.create_user(email=email,username=username,password=password)
        user.save()
        messages.success(request, 'User created successfully')
        
        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')
    


def login_view(request):

    if request.method=='POST':
        
        username=request.POST.get('loginusername')
        password=request.POST.get('loginpassword')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials,Please try again')
            return redirect('/')

    return HttpResponse('404 - Not Found')


def logout_view(request):
    
        logout(request)
        messages.success(request, 'Logged out successfully')
        return redirect('/')

        return HttpResponse('logout')




