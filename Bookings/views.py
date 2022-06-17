from .serializers import BookingsSerializer
from Administrator.models import Bookings
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt 

 
@csrf_exempt
class BookingsDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        
        # Saving information into College details table
        prod=Bookings()
        prod.bookings_package_id_id=request.POST.get('bookings_package_id')
        prod.bookings_traveller_id_id=request.POST.get('bookings_traveller_id')
        prod.bookings_booking_quantity=request.POST.get('bookings_booking_quantity')
        prod.bookings_booking_status='Pending'
        prod.bookings_organisation_userName_id=request.POST.get('bookings_organisation_userName')
        prod.save()
        
        return HttpResponse("Success")


    @csrf_exempt
    def BookingsTravellersList(request):
        bookings_traveller_id = request.POST.get('bookings_traveller_id')
        print(bookings_traveller_id)
        Bookings1=Bookings.objects.filter(bookings_traveller_id = bookings_traveller_id).all()
        serializer = BookingsSerializer(Bookings1, many = True)
        total_BookingsDetails1 = json.dumps(serializer.data)
        total_BookingsDetails = json.loads(total_BookingsDetails1)
        data = {'Bookings':total_BookingsDetails}
        return JsonResponse(data)


    @csrf_exempt
    def BookingsList(request):
        bookings_organisation_userName = request.POST.get('bookings_organisation_userName')
        print(bookings_organisation_userName)
        Bookings1=Bookings.objects.filter(bookings_organisation_userName = bookings_organisation_userName).all()
        serializer = BookingsSerializer(Bookings1, many = True)
        total_BookingsDetails1 = json.dumps(serializer.data)
        total_BookingsDetails = json.loads(total_BookingsDetails1)
        data = {'Bookings':total_BookingsDetails}
        return JsonResponse(data)


    # Getting  College Details from database 
    @csrf_exempt
    def BookingsDetails(request):
        bookings_booking_id = request.POST.get('bookings_booking_id') 
        print(bookings_booking_id)
        Bookings1=Bookings.objects.filter(id = bookings_booking_id).all()
        serializer = BookingsSerializer(Bookings1, many = True)
        total_BookingsDetails1 = json.dumps(serializer.data)
        total_BookingsDetails = json.loads(total_BookingsDetails1)
        data = {'BookingsDetails':total_BookingsDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def updateBookingStatus(request):       

        Bookings.objects.filter(bookings_booking_id = request.POST.get('bookings_booking_id')).update(
        bookings_booking_status=request.POST.get('bookings_booking_status'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt
    def updateBookingQuantity(request):       
        
        Bookings.objects.filter(bookings_booking_id = request.POST.get('bookings_booking_id')).update(
        bookings_booking_quantity=request.POST.get('bookings_booking_quantity'),
        )
        
        return HttpResponse("Success")    
    