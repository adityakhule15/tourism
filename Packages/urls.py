from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.PackageDetailsList.postSave, name="postSave"),
        path('packagedetails/', views.PackageDetailsList.PackageDetails, name="packagedetails"),
        path('update/', views.PackageDetailsList.update, name="update"),
        path('packageList/', views.PackageDetailsList.PackageList, name="packageList"),
        path('packageAvailable/', views.PackageDetailsList.PackageAvailable, name="packageAvailable"),
    ]