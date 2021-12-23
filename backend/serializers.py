from rest_framework import serializers
from backend.models import Transformer

class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformer
        fields = [
                  'TimeStamp', 'Transformer_ID', 'Current_Input', 
                  'Voltage_Input', 'Oil_Temprature', 'Winding_Temprature', 'Oil_TankLevel', 
                  'Moisture_Level', 'Tapping_Ratio', 'Overall_Health'
                  ]
