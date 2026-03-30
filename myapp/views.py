from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader


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