from django.db import models
from login.models import Account
# Create your models here.
CODE_CHOICES = [
    ('01', "Resedential Rural"),
    ('02', "Resedential Urban"),
    ('03', "Industrial"),
]


class Transformer(models.Model):
    id = models.AutoField(primary_key=True)
    Transformer_ID = models.CharField(max_length=50, unique=True)
    Transformer_Type = models.CharField(max_length=2, choices=CODE_CHOICES)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    accounts = models.ManyToManyField(Account)

    def __str__(self) -> str:
        return str(self.id)


class TransData(models.Model):
    id = models.BigAutoField(primary_key=True)
    TimeStamp = models.DateTimeField(auto_now_add=True)
    Current_Input = models.FloatField()
    Voltage_Input = models.FloatField()
    Oil_Temprature = models.FloatField()
    Winding_Temprature = models.FloatField()
    Oil_TankLevel = models.FloatField()
    Moisture_Level = models.FloatField()
    Tapping_Ratio = models.FloatField()
    Overall_Health = models.FloatField()
    transformer = models.ForeignKey(
        Transformer, related_name='transformer', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(str(self.transformer) + " || " + str(self.id))
