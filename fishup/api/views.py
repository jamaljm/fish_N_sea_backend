from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import customer, retailers, fishermen, fish1, fish2
from .serializers import customerserializer, retailerserializer, fishermanserializer, fishserializer, fishserializer2
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

# listing

class customerlist(ListAPIView):
    queryset = customer.objects.all()
    serializer_class = customerserializer

class retailerslist(ListAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer

class fishermanlist(ListAPIView):
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer

class fishlist(ListAPIView):
    queryset = fish1.objects.all()
    serializer_class = fishserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

#  creating

class customerlist(CreateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerserializer

class retailerslist(CreateAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer

class fishermanlist(CreateAPIView):
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer


# by 