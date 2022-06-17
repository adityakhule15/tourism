
from datetime import datetime
from .serializers import PackageSerializer
from Administrator.models import Packages
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings


@csrf_exempt
class PackageDetailsList(APIView):
    # Defining the function for posting PackagesDetails

    @csrf_exempt
    def postSave(request):
        # Saving information into Packagesdetails table
        userName=request.POST.get('packages_organisation_userName')
        title=request.POST.get('packages_title_of_package')
        prod=Packages()
        prod.packages_title_of_package=title
        prod.packages_description=request.POST.get('packages_description')
        prod.packages_budget=request.POST.get('packages_budget')
        prod.packages_places_to_visit=request.POST.get('packages_places_to_visit')
        prod.packages_cities_we_stay=request.POST.get('packages_cities_we_stay')
        prod.packages_pickup_point=request.POST.get('packages_pickup_point')
        prod.packages_drop_point=request.POST.get('packages_drop_point')
        prod.packages_duration=request.POST.get('packages_duration')
        prod.packages_package_highlights=request.POST.get('packages_package_highlights')
        prod.packages_organisation_userName_id=userName
        image=request.POST['image'],
        print(image[0])
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/Packages_image/' + userName + title + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        prod.packages_images1='/Packages_image/' + userName + title + '.jpeg'
        prod.save()
        
        return HttpResponse("Success")
        
    # Getting  PackagesDetails from database 
    @csrf_exempt
    def PackageDetails(request):
        id = request.POST.get('packages_id_of_package')
        print(id)
        PackageDetails1=Packages.objects.filter(id = id).all()
        serializer = PackageSerializer(PackageDetails1, many = True)
        total_PackageDetails1 = json.dumps(serializer.data)
        total_PackageDetails = json.loads(total_PackageDetails1)
        data = {'PackageDetails':total_PackageDetails}
        return JsonResponse(data)

    @csrf_exempt
    def PackageAvailable(request):
        Packages1=Packages.objects.all()
        serializer = PackageSerializer(Packages1, many = True)
        total_PackageDetails1 = json.dumps(serializer.data)
        total_PackageDetails = json.loads(total_PackageDetails1)
        data = {'PackageDetails':total_PackageDetails}
        return JsonResponse(data)

    # @csrf_exempt
    # def PackageAvailable(request):
    #     packages_pickup_point = request.POST.get('packages_pickup_point')
    #     print(packages_pickup_point)
    #     Packages1=Packages.objects.filter(packages_pickup_point = packages_pickup_point).all()
    #     serializer = PackageSerializer(Packages1, many = True)
    #     total_PackageDetails1 = json.dumps(serializer.data)
    #     total_PackageDetails = json.loads(total_PackageDetails1)
    #     data = {'PackageDetails':total_PackageDetails}
    #     return JsonResponse(data)

    @csrf_exempt
    def PackageList(request):
        packages_organisation_userName = request.POST.get('packages_organisation_userName')
        print(packages_organisation_userName)
        Packages1=Packages.objects.filter(packages_organisation_userName = packages_organisation_userName).all()
        serializer = PackageSerializer(Packages1, many = True)
        total_PackageDetails1 = json.dumps(serializer.data)
        total_PackageDetails = json.loads(total_PackageDetails1)
        data = {'PackageList':total_PackageDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        Packages.objects.filter(id = request.POST.get('packages_id_of_package')).update(
        packages_title_of_package=request.POST.get('packages_title_of_package'),
        packages_description=request.POST.get('packages_description'),
        packages_budget=request.POST.get('packages_budget'),
        packages_places_to_visit=request.POST.get('packages_places_to_visit'),
        packages_cities_we_stay=request.POST.get('packages_cities_we_stay'),
        packages_pickup_point=request.POST.get('packages_pickup_point'),
        packages_drop_point=request.POST.get('packages_drop_point'),
        packages_duration=request.POST.get('packages_duration'),
        packages_package_highlights=request.POST.get('packages_package_highlights'),
        )
        
        return HttpResponse("Success")    

    

