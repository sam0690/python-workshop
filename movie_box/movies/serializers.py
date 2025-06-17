from rest_framework import serializers  
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  # or specify fields like ('id', 'title', 'description', etc.)