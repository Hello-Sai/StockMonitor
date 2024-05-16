from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import WatchList
from accounts.serializers import UserSerializer, WatchListSerializer
from rest_framework.authentication import authenticate,SessionAuthentication
from django.contrib.auth import login,logout
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer  = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.instance)
            WatchList.objects.create(user_id = serializer.instance.id)
            # return Response("\nYour username is %s\nYour password is %s"%(username,password))
            return Response("Registered Successfully",status=202)
        return Response(serializer.errors,status=400)

class LoginView(APIView):
    def post(self,request):
        # print(request.data)
        user = authenticate(**request.data)
        if not user:
            return Response("Invalid Username / Password",status=400)
        login(request,user)
        print("user details ,",user.id,user)
        # return Response("\nYour username is %s\nYour password is %s"%(username,password))
        response =  Response("Logged In Successfully")
        response.set_cookie('userId',user.id)
        print(response.cookies)
        return response
    
class LogoutView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = [IsAuthenticated]
    def get(self,request):
        logout(request)
        # print(request.data,request.session,request)
        response =  Response("Successfully Logged Out\n %s"%request.session)
        response.delete_cookie('userId')
        return response
        
    
