from django.db import models
from django.core.mail import EmailMessage

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
        msg = EmailMessage(
            'Поступил заказ на сумму {}'.format(str(self.total_price)),
            """
            Заказчик: {}
            Телефон: {}
            Адрес: {}
            Комментарий к заказу: {}
            """.format(str(self.fullname), str(self.tel), str(self.address), str(self.comments)),
            to=['orders@mebelyes.store', 'dozor52@mail.ru'])
        msg.send()
        
    def save(self, *args, **kwargs):
        self.SendEmail()
        super(Order, self).save(*args, **kwargs)
