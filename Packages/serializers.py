from Administrator.models import Packages
from Administrator.serializers import AdministratorSerializer
from rest_framework import serializers


class OnlyPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    packages_organisation_userName = AdministratorSerializer()
    class Meta:
        model = Packages
        fields = '__all__'

