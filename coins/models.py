from django.db import models

# Create your models here.
class Coin(models.Model):
    SNo = models.IntegerField()
    Name = models.CharField(max_length=20)
    Symbol = models.CharField(max_length=10)
    Date = models.DateTimeField()
    High = models.FloatField()
    Low = models.FloatField()
    Open = models.FloatField()
    Close = models.FloatField()
    Volume = models.FloatField()
    Marketcap = models.FloatField()