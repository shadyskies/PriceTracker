from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .json_updater import json_update, main_price_getter_initial_json_create, check_json_exists
from .line_plot import plot
import os

# Create your views here.

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'links':obj
#     }


def get_links_view(request):
    form = ProductForm()
    if request.method == 'POST':
        username = str(request.user)
        print(username)
        form = ProductForm(request.POST)
        # form.save()
        # print("valid form")
        links = request.POST.get("links")
        if check_json_exists(username=username):
            json_update(url=links, username=username)
        else:
            main_price_getter_initial_json_create(username=username, url=links)
    context = {
        "form": form
    }
    return render(request, "products/get_links.html", context)


def get_dashboard(request):
    print(os.listdir("../plots/"))
    # context = {"image": "../plots/test.png"}
    if request.method == 'POST':
        username = str(request.user)
        plot(username=username)
    return render(request, "products/dashboard.html", {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/register.html", context)
