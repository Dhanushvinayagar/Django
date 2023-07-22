from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category

# Create your views here.
def home(request):
    return HttpResponse('HOME <a href="category/">GOTO</a>')


def category(request):
    cat=Category.objects.all()
    return render(request,'category.html',{"datas":cat})

def product(request,pk):
    cat=Product.objects.all().filter(key=pk)
    return render(request,'product.html',{"datas":cat})
