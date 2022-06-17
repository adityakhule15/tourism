
from .serializers import TravellerSerializer
from Administrator.models import Traveller, Login
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings

 
@csrf_exempt
class TravellerDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        usname = request.POST.get('traveller_userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.type_of_loginer = 'Traveller'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=Traveller()
        prod.traveller_userName_id=usname
        prod.traveller_name=request.POST.get('traveller_name')
        prod.traveller_gender=request.POST.get('traveller_gender')
        prod.traveller_dob=request.POST.get('traveller_dob')
        prod.traveller_mobileNumber=request.POST.get('traveller_mobileNumber')
        prod.traveller_email=request.POST.get('traveller_email')
        prod.traveller_address=request.POST.get('traveller_address')
        image=request.POST['image'],
        print(image[0])
        imgdata = base64.b64decode(image[0])
        print(usname)
        path = settings.MEDIA_ROOT + '/travellers_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        prod.traveller_image='/travellers_images/' + usname + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def TravellerDetails(request):
        traveller_userName = request.POST.get('traveller_userName')
        print(traveller_userName)
        TravellerDetails1=Traveller.objects.filter(traveller_userName = traveller_userName).all()
        serializer = TravellerSerializer(TravellerDetails1, many = True)
        total_TravellerDetails1 = json.dumps(serializer.data)
        total_TravellerDetails = json.loads(total_TravellerDetails1)
        data = {'TravellerDetails':total_TravellerDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        Traveller.objects.filter(traveller_userName = request.POST.get('traveller_userName')).update(
        traveller_name=request.POST.get('traveller_name'),
        traveller_gender=request.POST.get('traveller_gender'),
        traveller_email=request.POST.get('traveller_email'),
        traveller_dob=request.POST.get('traveller_dob'),
        traveller_mobileNumber=request.POST.get('traveller_mobileNumber'),
        traveller_address=request.POST.get('traveller_address'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt 
    def updateImage(request):
    
        usname=request.POST.get('traveller_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/travellers_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  

