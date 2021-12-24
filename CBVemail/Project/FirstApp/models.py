from django.db import models

class Laptop(models.Model):
    company=models.CharField(max_length=20)
    model_name=models.CharField(max_length=20)
    ram=models.IntegerField()
    rom=models.IntegerField()
    processor=models.CharField(max_length=20)
    price=models.FloatField()
    weight=models.FloatField()
