from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path("", include("myapp.urls")), 
    path("admin/", admin.site.urls),
    path("abcd/", views.abcd, name='abcd'),
    path("aman/", views.aman, name='aman'),
    path("mypage/", views.mypage, name='mypage'),
]