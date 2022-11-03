from multiprocessing import context
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'home.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        suggestion=request.POST['suggestion']

        stuff= contacttable(name=name, email=email,suggestion=suggestion)
        stuff.save()
    
    return render(request,'contact.html')


@login_required
def blog(request):
    if request.method=='POST':
        fm= postfunction(request.POST)
        if fm.is_valid():
            fm.save()
            fm= postfunction()
    else:
        fm= postfunction()
    totalposts=Post.objects.all()

    return render(request,'blog.html',{'form':fm, 'totalposts': totalposts})
 
# function for searching the blogs
def search(request):
    query = request.POST['query']
    totalposts= Post.objects.filter(title__icontains=query)
    params={'allposts': totalposts}
    return render(request,'search.html',params)

# yourblog
@login_required
def yourblog(request):
    totalposts= Post.objects.filter(author__icontains=request.user)
    params={'totalposts':totalposts}
    return render(request,'yourblog.html',params)



# for updateing the record 
@login_required
def update(request,sno):
    if request.method=='POST':
        pi= Post.objects.get(pk=sno)
        fm =postfunction(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi= Post.objects.get(pk=sno)
            fm= postfunction(instance=pi) 
    return render (request,'update.html',{'form':fm})



# for deleting the data
@login_required
def deleteblog(request,sno):
    if request.method=='POST':
        deletedata=Post.objects.get(pk=sno)
        deletedata.delete()
        return redirect('yourblog')








# AUTHENTICATION funcions 

def handlesignup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for input
        
        if pass1 != pass2:
            messages.error(request,'your both password are not same')
            return redirect('/')    
        # create the user
        myuser= User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'your account has been created')
        return redirect('/')
    else:
        return HttpResponse('not allowed')


def handlelogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password= loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request,'you are successfully logged in')
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')   
            return redirect('home')
    return redirect('home')


def handlesignout(request):
    logout(request)
    messages.success(request,'sucessfully logged out')
    return redirect('home')    



    
