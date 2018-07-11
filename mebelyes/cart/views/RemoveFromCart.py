from django.http import HttpResponse


def RemoveFromCart(request):
    cart = request.session['cart']
    total_price = int(request.session['total_price'])
    for pt in cart:
        if pt['id'] == request.POST.get('num[id]') and pt['name'] == request.POST.get('num[name]') and pt[
            'size'] == request.POST.get('num[size]') and pt['material'] == request.POST.get('num[material]') and pt[
            'color'] == request.POST.get('num[color]'):
            total_price -= int(pt['price'])
            for i in pt['services']:
                total_price -= int(i['price'])
            cart.remove(pt)
            break
    request.session['cart'] = cart

    request.session['total_price'] = total_price

    return HttpResponse('OK', status=200);