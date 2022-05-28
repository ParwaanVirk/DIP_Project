# Create your views here.
from rest_framework.permissions import IsAuthenticated
from backend.models import TransData, Transformer
from backend.serializers import TransformerSerializer, TransDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.MongoFetcher import get_database 


class TransformerAllView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cuser = request.user
        if cuser != None:
            t_list = Transformer.objects.filter(accounts=cuser)
            serialized_t_list = TransformerSerializer(t_list, many=True)
            return Response(data=serialized_t_list.data, status=200)
        else:
            return Response(data="No user exists", status=300)


class TransData_Particular_View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cuser = request.user
        if cuser != None:
            trans_id = request.data.get('trans_id', None)
            transformer_object = Transformer.objects.filter(id=trans_id)[0]
            print("HEllo ....*********")
            print(transformer_object)
            transformer_params_objects = TransData.objects.filter(
                transformer=transformer_object)
            print(transformer_params_objects)
            serialized_params_list = TransDataSerializer(
                transformer_params_objects, many=True)
            return Response(data=serialized_params_list.data, status=200)
        else:
            return Response(data="NO transdata exists", status=300)



class MongoDbFeeder(APIView):
    def get(self, request, *args, **kwargs):
        # cuser = request.user
        # if cuser != None:
        get_database()
        return Response(data = "Successfull", status = 200)
