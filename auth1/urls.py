from unicodedata import name
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('user_home', views.user_home, name="user_home"),
    path('signout', views.signout, name="signout"),
    path('adminpro', views.adminpro, name="adminpro"),
    path('funcupdate<int:pk>', views.funcupdate, name="funcupdate"),
    path('fundelete<int:pk>', views.fundelete, name="fundelete"),
    path('adduser', views.adduser, name="adduser"),
    path('search',views.search,name="search"),
    path('adminprologin', views.adminprologin, name="adminprologin"),
    path('adminprologout',views.adminprologout,name="adminprologout"),
    

]
