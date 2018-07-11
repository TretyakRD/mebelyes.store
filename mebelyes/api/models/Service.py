from django.db import models


class Service(models.Model):
    description = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)

