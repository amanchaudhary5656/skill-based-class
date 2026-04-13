from email import message
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db import IntegrityError
from django.contrib import messages
from .models import MyTable



# Create your views here.
def abcd(request):
    return HttpResponse('Hello, World!')
def aman(request):
    return HttpResponse('Welcome to Django!')

def mypage(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))
def number_view(request):
    numbers = [1, 2, 3, 4, 5]
    return render(request, "numbers.html", {"numbers": numbers})
def insert_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        
        try:
            MyTable.objects.create(name=name, subject=subject, email=email)
            message.success(request, "Data inserted successfully!")
        except IntegrityError:
            message.error(request, "Email Already exists!")
            return render(request, "form.html",{"error": "Email already exists!"})
        return render("insert")
    return render(request, "form.html")