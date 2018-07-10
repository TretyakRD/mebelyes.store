from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    prices = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    material = models.CharField(max_length=256)
    sizes = models.CharField(max_length=256)
    services = models.ManyToManyField('Service', blank=True)
    img_url = models.CharField(max_length=256, blank=True, editable=False)

    def FillUrl(self):
        self.img_url = 'api/img/' + str(self.category) + '/' + str(self.slug) + '.jpg'
        print(self.img_url)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.FillUrl()
        super(Product, self).save(*args, **kwargs)