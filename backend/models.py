from django.db import models

# Create your models here.
CODE_CHOICES = [
    ('01', "Resedential Rural"),
    ('02', "Resedential Urban"),
    ('03', "Industrial"),
]

class Transformer(models.Model):
    id = models.AutoField(primary_key=True)
    TimeStamp = models.DateTimeField(auto_now_add=True)
    Transformer_ID = models.CharField(max_length=50, )
    Locality = models.CharField(max_length=2, choices=CODE_CHOICES)
    Current_Input = models.FloatField()
    Voltage_Input = models.FloatField()
    Oil_Temprature = models.FloatField()
    Winding_Temprature = models.FloatField()
    Oil_TankLevel = models.FloatField()
    Moisture_Level = models.FloatField()
    Tapping_Ratio = models.FloatField()
    Overall_Health = models.FloatField()

    def __str__(self) -> str:
        return self.Transformer_ID