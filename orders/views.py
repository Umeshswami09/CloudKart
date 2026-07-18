from django.shortcuts import render, redirect
from .models import Order
from cart.models import Cart
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    if request.method == "POST":

        Order.objects.create(

            user=request.user,

            full_name=request.POST["full_name"],

            phone=request.POST["phone"],

            address=request.POST["address"],

            city=request.POST["city"],

            payment_method=request.POST["payment"],

            total_amount=total

        )

        return redirect("success")

    return render(request, "orders/checkout.html", {

        "cart_items": cart_items,

        "total": total

    })


def success(request):
    return render(request, "orders/success.html")