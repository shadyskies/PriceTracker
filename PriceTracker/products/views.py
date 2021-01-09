from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'links':obj
#     }


def get_links_view(request):
    form = ProductForm()
    print(request.POST)
    context = {
        "form": form
    }
    return render(request, "products/get_links.html", context)
