from django.shortcuts import render

from ..order import SrlzOrder


def Add(request):
    try:
        if(request.method!='POST'):
            raise
        order = SrlzOrder(request)
        if order is None:
            raise

        order.save()
        request.session['cart']=[]
        request.session['total_price']=0
        return render(request, 'cart_order/Add.html', {'text': "Заказ успешно добавлен, ожидайте звонка оператора"})
    except:
       return render(request, 'cart_order/Add.html', {'text': "Что-то пошло не так("})