from django.http.response import HttpResponse
from rest_framework.views import APIView
from Administrator.models import Administrator, Login, Traveller
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from Administrator.serializers import AdministratorSerializer
from Traveller.serializers import TravellerSerializer

# Create your views here
@csrf_exempt
class ForgotpasswordandCreatpassword(APIView):
    @csrf_exempt
    def creatpassword(request):
        frProd = Login()
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        Login.objects.filter(userName = request.POST.get('userName')).update(password=new_key,salt = sha_salt)
        return HttpResponse("Success")
        
    @csrf_exempt
    def otpVerification(request):
        OTP=request.POST.get('OTP')
        print(OTP)
        if OTP == '6543':
            return HttpResponse("Success")
        return HttpResponse("Failure")

    #posting a input data for checking   
    @csrf_exempt
    def forgotpassword(request):
        userName=request.POST.get('userName')
        position=request.POST.get('type_of_loginer') 
        print('Position:-' + position)
        email=request.POST.get('email')
        # print("Mai aaa rha hu...................................:")

        if position == 'Administrator':
            LoginDetails1=Administrator.objects.filter(administrator_userName=userName,administrator_email=email).all()
            serializer = AdministratorSerializer(LoginDetails1, many = True)
            total_LoginDetails1 = json.dumps(serializer.data)
            total_LoginDetails = json.loads(total_LoginDetails1)
            if len(total_LoginDetails) > 0:
                print("Success")
                #need to call otp url
                return HttpResponse("Success")

        elif position == 'Traveller':
            LoginDetails1=Traveller.objects.filter(traveller_userName=userName,traveller_email=email).all()
            serializer = TravellerSerializer(LoginDetails1, many = True)
            total_LoginDetails1 = json.dumps(serializer.data)
            total_LoginDetails = json.loads(total_LoginDetails1)
            if len(total_LoginDetails) > 0:
                print("Success")
                #need to call otp url
                return HttpResponse("Success")

        return HttpResponse("Failure")

       