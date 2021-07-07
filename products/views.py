from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.object.get()
    return render(request, "product/detail.html", {})