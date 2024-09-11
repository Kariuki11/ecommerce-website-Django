from urllib import request
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


# Create your views here.
def home(request):
    return render (request, "app/home.html")

class CategoryView(View):
    def get (self,request,val):
        return render(request, "app/category.html",locals())
