from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index_2, name='index_2'),
    path('certifications', views.certifications, name='certifications'),
    path('about', views.company_profile, name='about'),
    path('products', views.products_v2, name='products'),

    path('sitemap.xml', sitemap, 
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

    # path('index', views.index, name='index'),
    # path('tech_service', views.tech_service, name='tech_service'),
    # path('about', views.about, name = 'about'), 
    # path('news', views.news, name = 'news'),
    # path('news_detal', views.news_detail, name= 'news_detail'),
    # path('team', views.team, name = 'team'), 
    # path('values', views.values, name = 'values'), 
    # path('products', views.products, name = 'products'), 
    # path('products_cushion', views.products_cushion, name = 'products_cushion'), 
    # path('products_door_curtain', views.products_door_curtain, name = 'products_door_curtain'), 
    # path('products_shower_curtain', views.products_shower_curtain, name = 'products_shower_curtain'), 
    # path('products_tablecloth', views.products_tablecloth, name = 'products_tablecloth'), 
    # path('products_wall_covering', views.products_wall_covering, name = 'products_wall_covering'), 
    # path('products_wall_picture', views.products_wall_picture, name = 'products_wall_picture'), 
]