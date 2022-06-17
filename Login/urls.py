from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.LoginDetailsList.postSave, name="postSave"),
        path('login/', views.LoginDetailsList.login, name="login"),
        path('changePassword/', views.LoginDetailsList.changePassword, name="changePassword"),
    ]