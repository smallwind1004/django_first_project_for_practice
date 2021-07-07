from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product
    context = {
        'title': obj.title,
        'discription': obj.discription,
        'price': obj.price
    }
    return render(request, "product/detail.html", {})