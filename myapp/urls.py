from django.urls import path
from . import views

urlpatterns = [
    path("abcd/", views.abcd, name="abcd"),
    path("aman/", views.aman, name="aman"),
    path("mypage/", views.mypage, name="mypage"),
    path("numbers/", views.number_view, name="number_view"),
    path("insert/", views.insert_data, name="insert_data"),
]