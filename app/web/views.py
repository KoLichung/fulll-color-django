from django.shortcuts import redirect, render
from django.http import HttpResponse

# ============ Version 2 ==================
def index_2(request):
    return render(request,'web/index_2.html')

def certifications(request):
    return render(request,'web/certifications.html')

def company_profile(request):
    return render(request,'web/company_profile.html')

def products_v2(request):
    return render(request,'web/products_v2.html')

def redirect_to_about(request):
    return redirect('about')

# ============ Version 1 ==================

def index(request):
    return render(request,'web/index.html')

def tech_service(request):
    return render(request,'web/tech_service.html')

def about(request):
    return render(request,'web/about.html')

def news(request):
    return render(request,'web/news.html')

def news_detail(request):
    return render(request,'web/news_detail.html')

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

