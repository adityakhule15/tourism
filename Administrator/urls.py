from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.AdministratorDetailsList.postSave, name="postSave"),
        path('administratordetails/', views.AdministratorDetailsList.AdministratorDetails, name="administratordetails"),
        path('update/', views.AdministratorDetailsList.update, name="update"),
        path('updateImage/', views.AdministratorDetailsList.updateImage, name="updateImage"),
    ]