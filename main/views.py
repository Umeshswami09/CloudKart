from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db.models import Q

from .models import Product


def home(request):
    print("HOME VIEW CALLED")
    products = Product.objects.all()

    return render(request, "home.html", {
        "products": products
    })


def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account Created Successfully")
        return redirect("login")

    return render(request, "accounts/register.html")


def login_page(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid Username or Password")

    return render(request, "accounts/login.html")


def logout_page(request):

    logout(request)

    return redirect("home")


def products(request):

    products = Product.objects.all()

    return render(request, "products.html", {
        "products": products
    })


def categories(request):

    return render(request, "categories.html")


def about(request):

    return render(request, "about.html")


def contact(request):

    return render(request, "contact.html")


# -------------------------
# PRODUCT DETAILS
# -------------------------

def product_detail(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]

    return render(request, "product_detail.html", {
        "product": product,
        "related_products": related_products
    })


# -------------------------
# AJAX SEARCH
# -------------------------

def search_products(request):

    query = request.GET.get("q", "")

    products = Product.objects.filter(

        Q(name__icontains=query) |
        Q(category__icontains=query) |
        Q(description__icontains=query)

    )[:8]

    data = []

    for product in products:

        data.append({

            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "image": product.image.url,

        })

    return JsonResponse(data, safe=False)