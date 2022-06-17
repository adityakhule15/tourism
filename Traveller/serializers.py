from Administrator.models import Traveller
from rest_framework import serializers

class TravellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveller
        fields = '__all__'

