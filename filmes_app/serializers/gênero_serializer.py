from rest_framework import serializers
from ..models import Gênero

class GêneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gênero
        fields = '__all__'