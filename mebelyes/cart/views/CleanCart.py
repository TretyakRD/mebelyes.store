from django.http import HttpResponse


def CleanCart(request):
    if request.method == 'POST':
        request.session['cart'] = []
        request.session['total_price'] = 0
        return HttpResponse('OK', status=200)
    else:
        return HttpResponse('...', status=500)