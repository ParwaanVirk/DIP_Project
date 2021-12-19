
# Create your views here.
from rest_framework.decorators import api_view
from backend.models import Transformer
from backend.serializers import TransformerSerializer
from rest_framework.response import Response


@api_view(['POST', ])
def TransformerDataAll(request):
    if request.mehod == 'POST':
        LatestData = Transformer.objects.order_by('-TimeStamp')
        SerializedData = TransformerSerializer(LatestData, many = True)
        return Response(SerializedData.data)
    else:
        return Response(data = "Wrong Request", status = 300)
    
@api_view(['POST', ])
def TransformerLocality(request):
    if request.mdehod == "POST":
        loc_type = request.data['loc_type']
        if loc_type == '01' or loc_type == '02' or loc_type == '03':
            LatestData = Transformer.objects.filter(Locality = loc_type).order_by('-TimeStamp')
            SerializedData = TransformerSerializer(LatestData, many = True)
            return Response(SerializedData.data)
        else:
            return Response(data = "Wrong locality Type Passed", status = 400)
    else:
        return Response(data = "Wrong request Type", status = 300)    




@api_view(['POST', ])
def TransformerByID(request):
    if request.mdehod == "POST":
        TransID = request.data['TransID']
        
        LatestData = Transformer.objects.filter(Transformer_ID = TransID).order_by('-TimeStamp')
        SerializedData = TransformerSerializer(LatestData, many = True)
        return Response(SerializedData.data)
    else:
        return Response(data = "Wrong request Type", status = 300)    


