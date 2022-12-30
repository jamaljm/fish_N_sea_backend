from rest_framework import serializers
from .models import customer, retailers, fishermen, fish1, fish2,fishcount


class fishserializer(serializers.ModelSerializer):
    class Meta:
        model = fish1
        fields = ('id', 'name', 'price', 'description', 'retailers','fishermen') 


class fishermanserializer(serializers.ModelSerializer):
    class Meta:
        model = fishermen
        fields = ('id', 'name', 'email', 'location', 'password', 'password2')


class retailerserializer(serializers.ModelSerializer):
    class Meta:
        model = retailers
        fields = ('id', 'name', 'email', 'location', 'password', 'password2')


class customerserializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('id', 'name', 'email', 'location', 'password', 'password2')


class fishserializer2(serializers.ModelSerializer):
    class Meta:
        model = fish2
        fields = ('id', 'name', 'price', 'description', 'user') 


class fishcountserializer(serializers.ModelSerializer):
    class Meta:
        model = fishcount
        fields = ('id', 'name')