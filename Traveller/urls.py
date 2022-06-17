from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.TravellerDetailsList.postSave, name="postSave"),
        path('travellerdetails/', views.TravellerDetailsList.TravellerDetails, name="travellerdetails"),
        path('update/', views.TravellerDetailsList.update, name="update"),
        path('updateImage/', views.TravellerDetailsList.updateImage, name="updateImage"),
    ]