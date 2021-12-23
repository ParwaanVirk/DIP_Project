from backend.OverallHealth import get_health
from backend.models import Transformer

TransList = Transformer.objects.all()

for Trans in TransList:
    health = get_health(
    Trans.Transformer_ID, 
    Trans.Current_Input, 
    Trans.Voltage_Input, 
    Trans.Oil_Temprature, 
    Trans.Winding_Temprature, 
    Trans.Moisture_Level,
    )
    Trans.Overall_Health = health
    Trans.save()


