from django.core.mail import send_mail
from django.db import models


class Order(models.Model):
    fullname = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    tel = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField()
    comments = models.TextField(max_length=256)
    cart = models.TextField(max_length=2048)
    def SendEmail(self):
        send_mail(
            'Новый заказ!',
            'Поступил заказ на сумму '+str(self.total_price),
            'orders@mebelyes.store',
            ['orders@mebelyes.store', 'dozor52@mail.ru'],
            fail_silently=False,
        )

    def save(self, *args, **kwargs):
        self.SendEmail()
        super(Order, self).save(*args, **kwargs)
