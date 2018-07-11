from django.shortcuts import render


def GetCart(request):
    if 'cart' in request.session:
        cart = request.session['cart']
        total_price = request.session['total_price']
        return render(request, 'cart/GetCart.html', {'cart': cart, 'total_price': total_price})
    else:
        return render(request, 'cart/GetCart.html', {'cart': 'В вашей корзине пока пусто'})