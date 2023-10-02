from rest_framework import serializers
from ..models import Filme
from .gênero_serializer import GêneroSerializer

class FilmeSerializer(serializers.ModelSerializer):
    gênero = GêneroSerializer()
    class Meta:
        model = Filme
        fields = '__all__'