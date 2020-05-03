from rest_framework import serializers
from .models import State, City

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ('id', 'name', 'state_id')