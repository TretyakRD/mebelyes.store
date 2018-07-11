from django.shortcuts import render


def New(request):
    return render(request, 'cart_order/New.html')