# Generated by Django 2.0.7 on 2018-07-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180706_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
