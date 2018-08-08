from .models import Order
import json
def SrlzOrder(request):
    order = Order()
    try:
        order.fullname = request.POST.get('lastname') + ' ' + request.POST.get('name') + ' ' + request.POST.get('patronymic')
        order.email = request.POST.get('email')
        order.address = request.POST.get('address')
        order.tel = request.POST.get('tel')
        order.total_price = request.session['total_price']
        order.comments = request.POST.get('comments')
        order.cart = request.session['cart']
        return order
    except:
        return None