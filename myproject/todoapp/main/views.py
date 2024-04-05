from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task

# Create your views here.

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
    