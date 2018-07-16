from django.shortcuts import render


def New(request):
    total_price = 0
    if 'cart' in request.session:
        total_price = request.session['total_price']
        if total_price == 0:
            return render(request, 'cart_order/Add.html', {'text': "Ваша корзина пуста!"})
    else:
        return render(request, 'cart_order/Add.html', {'text': "Ваша корзина пуста!"})

    return render(request, 'cart_order/New.html', {'total_price': total_price})