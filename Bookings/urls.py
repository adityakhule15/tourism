from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.BookingsDetailsList.postSave, name="postSave"),
        path('bookingsdetails/', views.BookingsDetailsList.BookingsDetails, name="bookingsdetails"),
        path('BookingsTravellersList/', views.BookingsDetailsList.BookingsTravellersList, name="BookingsTravellersList"),
        path('BookingsList/', views.BookingsDetailsList.BookingsList, name="BookingsList"),
        path('updateBookingQuantity/', views.BookingsDetailsList.updateBookingQuantity, name="updateBookingQuantity"),
        path('updateBookingStatus/', views.BookingsDetailsList.updateBookingStatus, name="updateBookingStatus"),
    ]