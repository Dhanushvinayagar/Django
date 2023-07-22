from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.

#home of the project
def home(request):
    todos=Todo.objects.all()
    content={'todos':todos}
    return render(request,'home.html',content)

def add(request):
    return render(request,'add.html')

def update(request,pk):
    if request.method=="POST":
        name=request.POST.get("name")
        desc=request.POST.get("desc")
        u=Todo.objects.filter(id=pk).update(name=name,desc=desc)
    return redirect("home")


def edit(request,pk):
    e=Todo.objects.get(id=pk)
    return render(request,'edit.html',{"edit":e})

def added(request):
    if request.method=="POST":
        n=request.POST.get("num")
        na=(request.POST.get("name")).lower().capitalize()
        de=request.POST.get("desc")
        data=Todo(num=n,name=na,desc=de) 
        data.save()
    return redirect("home")

def delete(request,pk):
    d=Todo.objects.get(id=pk)
    d.delete() 
    return redirect("home")
    # data=pk
    # return render(request,"print.html",{"data":data})

def search(request):
    if request.method=="POST":
        val=request.POST.get("name").lower().capitalize()
        todos=Todo.objects.all().filter(name__icontains=val)
    return render(request,"home.html",{"todos":todos,"success":True})

def filter(request):
    todos=Todo.objects.all().order_by("name").values()
    content={'todos':todos,"success":True}
    return render(request,'home.html',content)
    
    