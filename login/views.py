from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from login.models import * 
from login.serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data.get('email'))
        print(request.data.get('username'))
        print(request.data.get('password'))
        requester = {
            'email': request.data.get('email', None),
            'username': request.data.get('username', None),
            'password' : request.data.get('password', None), 
        }
        serializer = RegistrationSerializer(data = requester)
        data = {}
        userType = "NO"
        if userType == "NO":
            if serializer.is_valid():
                Caccount = serializer.save()
                Caccount.is_normaluser = True
                Caccount.latitude = 32.333
                Caccount.longitude = 76.666                
                Caccount.save()
                data['response'] = "Successfully registered a new user"
                status = 200
            else:
                data = serializer.errors
                status = 422

        else:
            data = "Wrong data passed"
            status = 423
        
        return Response(data, status)


class UserDataView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):
        cuser = request.user
        cuserSerialized = UserSerializer(cuser)
        return Response(data = cuserSerialized.data, status=200)
    
    def post(self, request, *args, **kwargs):
        cuser = request.user
        if cuser != None and cuser.is_admin == True:
            UserList = Account.objects.all()
            SerialiezedUserList = UserSerializer(UserList, many= True)
            return Response(data = SerialiezedUserList.data, status = 200)
    

    def put(self, request, *args, **kwargs):
        cuser = request.user
        if cuser != None and cuser.is_admin == True:
            user_email = request.data.get('email', None)
            latitude = request.data.get('latitude', None)
            longitude = request.data.get('longitude', None)
            if Account.objects.filter(email = user_email).exists() == True:
                Mod_User = Account.objects.filter(email = user_email)[0]
                Mod_User.latitude = latitude
                Mod_User.longitude = longitude
                Mod_User.save()
            return Response(data = "Latitude and longitude updated", status=200)
        else:
            return Response(data = "Wrong user type", status = 200)
    




    
class PasswordReset(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, *args, **kwargs):
        cuser = request.user
        if cuser != None:
            serializer = ChangePasswordSerializer(data = request.data)
            if serializer.is_valid():
                oldPassword = serializer.validated_data['old_password']
                newPassword = serializer.validated_data['new_password']
                if not cuser.check_password(oldPassword):
                    return Response(data = "Old password was wrong", status=400)
                elif oldPassword == newPassword:
                    return Response(data= "Cannot keep same password", status = 420)
                else:
                    cuser.set_password(newPassword)
                    print(newPassword)
                    cuser.save()
                    return Response(status = 200, data = "Successfully updated password")
            else:
                return Response(data = serializer.errors, status = 430)
        else:
            return Response(data = "Cuser does not exist", status = 404)
            
  
class DeleteUsers(APIView):
    #list of email ids will be sent. 
    permission_classes=[IsAuthenticated]
    def post(self, request, *args, **kwargs):
        cuser = request.user
        if cuser != None and cuser.is_admin == True:
            list_of_emails = request.data.get('list_of_emails', None)
            if list_of_emails != None:

                for email in list_of_emails:
                    if Account.objects.filter(email = email).exists():
                        Account.objects.filter(email = email)[0].delete()

            return Response(data = "Users deleted", status = 200)
        else:
            return Response(data = "Wrong user", status = 200)
        


                



        



