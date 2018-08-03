from django.http import HttpResponse
from django.core.mail import EmailMessage


def test(request):
    msg = EmailMessage('Request Callback', 'Here is the message.', 'orders@mebelyes.store', to=['orders@mebelyes.store'])
    msg.send(fail_silently=False)
    return HttpResponse('OK')