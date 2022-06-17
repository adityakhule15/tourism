from Administrator.models import Bookings
from Administrator.serializers import AdministratorSerializer
from Packages.serializers import OnlyPackageSerializer
from Traveller.serializers import TravellerSerializer
from rest_framework import serializers

class BookingsSerializer(serializers.ModelSerializer):
    bookings_organisation_userName = AdministratorSerializer()
    bookings_package_id = OnlyPackageSerializer()
    bookings_traveller_id = TravellerSerializer()
    class Meta:
        model = Bookings
        fields = '__all__'

