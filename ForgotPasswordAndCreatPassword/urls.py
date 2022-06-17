from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('creatpassword/', views.ForgotpasswordandCreatpassword.creatpassword, name="creatpassword"),
        path('forgotpassword/', views.ForgotpasswordandCreatpassword.forgotpassword, name="forgotpassword"),
        path('otpVerification/', views.ForgotpasswordandCreatpassword.otpVerification, name="otpVerification"),
    ]