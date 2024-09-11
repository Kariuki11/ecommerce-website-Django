# from django.db.models import Count
# from django.shortcuts import render
# from django.views import View
# from .models import Product

# class CategoryView(View):
#     def get(self, request, val):
#         # Query the Product model
#         products = Product.objects.filter(category=val)
        
#         # Calculate title counts
#         title_counts = products.values('title').annotate(total=Count('title'))
        
#         # Pass variables to the template
#         context = {
#             'val': val,
#             'title_counts': title_counts
#         }
#         return render(request, "app/category.html", context)



























from django.db.models import Count
from django.shortcuts import render
# from django.views import View
# from . models import Product


# # Create your views here.
# def home(request):
#     return render (request, "app/home.html")

# class CategoryView(View):
#     def get (self,request,val):
#         product = Product.objects.filter(category=val)
#         title = product.objects.filter(category=val).values('title').annotate(total=Count('title'))
#         return render(request, "app/category.html",locals())
