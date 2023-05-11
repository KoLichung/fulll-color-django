from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')

def news(request):
    return render(request,'web/news.html')

def team(request):
    return render(request,'web/team.html')

def values(request):
    return render(request,'web/values.html')

def products(request):
    return render(request,'web/products.html')

def products_cushion(request):
    return render(request,'web/products_cushion.html')

def products_door_curtain(request):
    return render(request,'web/products_door_curtain.html')

def products_shower_curtain(request):
    return render(request,'web/products_shower_curtain.html')

def products_tablecloth(request):
    return render(request,'web/products_tablecloth.html')

def products_wall_covering(request):
    return render(request,'web/products_wall_covering.html')

def products_wall_picture(request):
    return render(request,'web/products_wall_picture.html')

