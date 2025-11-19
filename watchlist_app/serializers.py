from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    release_year = serializers.IntegerField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)   


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.release_year = validated_data.get('release_year', instance.release_year)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
    