from rest_framework import serializers
from backend.models import TransData, Transformer

class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformer
        fields = ['id', 'Transformer_ID', 'Transformer_Type', 'latitude', 'longitude']



class TransDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TransData
        fields = ['TimeStamp', 'Current_Input', 'Voltage_Input', 'Oil_Temprature', 'Winding_Temprature', 'Oil_TankLevel', 'Moisture_Level', 'Tapping_Ratio', 'Overall_Health']