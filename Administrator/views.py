from Administrator.serializers import AdministratorSerializer
from .models import Administrator, Login
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings

 
@csrf_exempt
class AdministratorDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        usname = request.POST.get('administrator_userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.type_of_loginer = 'Administrator'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=Administrator()
        prod.administrator_userName_id=usname
        prod.administrator_name_of_organization=request.POST.get('administrator_name_of_organization')
        prod.administrator_name_of_admin=request.POST.get('administrator_name_of_admin')
        prod.administrator_office_number=request.POST.get('administrator_office_number')
        prod.administrator_website=request.POST.get('administrator_website')
        prod.administrator_address=request.POST.get('administrator_address')
        prod.administrator_mobileNumber=request.POST.get('administrator_mobileNumber')
        prod.administrator_email=request.POST.get('administrator_email')
        prod.administrator_location_0f_organization=request.POST.get('administrator_location_0f_organization')
        image=request.POST['image'],
        print(image[0])
        imgdata = base64.b64decode(image[0])
        print(usname)
        path = settings.MEDIA_ROOT + '/administrators_image/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        prod.administrator_image='/administrators_image/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def AdministratorDetails(request):
        administrator_userName = request.POST.get('administrator_userName')
        print(administrator_userName)
        AdministratorDetails1=Administrator.objects.filter(administrator_userName = administrator_userName).all()
        serializer = AdministratorSerializer(AdministratorDetails1, many = True)
        total_AdministratorDetails1 = json.dumps(serializer.data)
        total_AdministratorDetails = json.loads(total_AdministratorDetails1)
        data = {'AdministratorDetails':total_AdministratorDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        Administrator.objects.filter(administrator_userName = request.POST.get('administrator_userName')).update(
        administrator_name_of_organization=request.POST.get('administrator_name_of_organization'),
        administrator_name_of_admin=request.POST.get('administrator_name_of_admin'),
        administrator_office_number=request.POST.get('administrator_office_number'),
        administrator_website=request.POST.get('administrator_website'),
        administrator_address=request.POST.get('administrator_address'),
        administrator_email=request.POST.get('administrator_email'),
        administrator_mobileNumber=request.POST.get('administrator_mobileNumber'),
        administrator_location_0f_organization=request.POST.get('administrator_location_of_organization'),
        )
       
        return HttpResponse("Success")    

    @csrf_exempt
    def updateImage(request):
    
        usname=request.POST.get('administrator_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/administrators_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  
