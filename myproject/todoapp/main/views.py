from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logoutuser(request):
    logout(request)
    return redirect("loginpage")

def registeruser(request):
    form=UserCreationForm();
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"An error occured")

    context={"form":form}
    return render(request,"login.html",context )
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("home")
    page="login"
    if request.method=="POST":
        username=request.POST.get("username")
        password= request.POST.get("password")

        try:
            user=User.objects.get(username=username)
            print(username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "username or password doesnt match")
        except:
            redirect("home")
            messages.error(request,"user not found")


    print(page)
    context={"page":page}
    return render(request,"login.html",context )





@login_required(login_url="loginpage")
def home(request):
    tasks=Task.objects.filter(is_complted=False)
    complted_task=Task.objects.filter(is_complted=True)
    context={"tasks":tasks,
             "completed":complted_task
             }
    return render(request,'home.html',context)

def completed(request,pk):
    task=Task.objects.get(id=pk)
    task.is_complted=True
    task.save()
    return redirect('home')

def incomplete(request,pk):  
    task=Task.objects.get(id=pk)
    task.is_complted=False
    task.save()
    return redirect('home')

def deletetask(request,pk):
    task=Task.objects.get(id=pk)

    task.delete()
    return redirect('home')

def addtask(request):
    if request.method=="POST":
        task=request.POST.get("task")
        todo=Task.objects.create(task=task)
        todo.save()
        return redirect("home")
    
def updatetask(request,pk):
    update_task=Task.objects.get(id=pk)
    print(update_task)
    if request.method=="POST":
        print("task")
        newtask=request.POST.get("new_task")
        print(newtask)
        update_task.task=newtask
        update_task.save()
        return redirect("home")
    else:
        print("else part")
        context ={"task":update_task} 
        return render(request,"update.html",context)

