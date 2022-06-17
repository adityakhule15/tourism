from django.db import models

' Models for Login Details '
class Login(models.Model):
    userName = models.CharField(max_length=100, primary_key= True)
    password = models.CharField(max_length=1000,null=True)
    type_of_loginer = models.CharField(max_length=1000,null=True)
    salt = models.CharField(max_length=1000, default='False')

    class Meta:
        db_table = "logins"



' Models for Administrator '    
class Administrator(models.Model):
    administrator_userName = models.ForeignKey(Login,primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    administrator_name_of_organization = models.CharField(max_length=1000,null=True) 
    administrator_name_of_admin = models.CharField(max_length=1000,null=True)
    administrator_mobileNumber = models.CharField(max_length=1000,null=True) 
    administrator_office_number = models.CharField(max_length=1000,null=True)
    administrator_email = models.CharField(max_length=1000,null=True)
    administrator_image = models.CharField(max_length=10000,null=True)
    administrator_address = models.CharField(max_length=1000,null=True) 
    administrator_website = models.CharField(max_length=1000,null=True) 
    administrator_location_0f_organization = models.CharField(max_length=1000,null=True) 

    class Meta:
        db_table = "administrator"



''' Models for Traveller '''
class Traveller(models.Model):
    traveller_userName = models.ForeignKey(Login, primary_key=True, default='unknown',on_delete=models.SET_DEFAULT)
    traveller_name = models.CharField(max_length=1000,null=True) 
    traveller_gender = models.CharField(max_length=1000,null=True) 
    traveller_dob = models.CharField(max_length=1000, default='1899-09-09')
    traveller_mobileNumber = models.CharField(max_length=1000,null=True) 
    traveller_email = models.CharField(max_length=1000,null=True) 
    traveller_image= models.CharField(max_length=10000,null=True)
    traveller_address = models.CharField(max_length=1000,null=True) 

    class Meta:
        db_table = "traveller"



''' Models for Packages '''
class Packages(models.Model):
    packages_title_of_package = models.CharField(max_length=1000,null=True)
    packages_description = models.CharField(max_length=1000,null=True)
    packages_budget = models.CharField(max_length=1000,null=True)
    packages_places_to_visit = models.CharField(max_length=1000,null=True)
    packages_cities_we_stay = models.CharField(max_length=1000,null=True)
    packages_pickup_point = models.CharField(max_length=1000,null=True)
    packages_drop_point = models.CharField(max_length=1000,null=True)
    packages_duration = models.CharField(max_length=1000,null=True)
    packages_package_highlights = models.CharField(max_length=1000,null=True)
    packages_no_of_bookings = models.CharField(max_length=1000,null=True)
    packages_organisation_userName = models.ForeignKey(Administrator, default= 'unknown', on_delete=models.SET_DEFAULT) 
    packages_images1 = models.CharField(max_length=10000,null=True)

    class Meta:
        db_table = "packages"


 
''' Models for Bookings '''
class Bookings(models.Model):
    bookings_package_id = models.ForeignKey(Packages, default= 'unknown', on_delete=models.SET_DEFAULT)
    bookings_traveller_id = models.ForeignKey(Traveller, default='unknown', on_delete=models.SET_DEFAULT)
    bookings_booking_quantity = models.CharField(max_length=100, default = '1')
    bookings_booking_status = models.CharField(max_length=100, default = False)
    bookings_organisation_userName = models.ForeignKey(Administrator, default= 'unknown', on_delete=models.SET_DEFAULT) 
    
    class Meta:
        db_table = "bookings"


