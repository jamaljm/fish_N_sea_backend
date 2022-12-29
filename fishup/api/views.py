

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import customer, retailers, fishermen, fish1, fish2
from .serializers import customerserializer, retailerserializer, fishermanserializer, fishserializer, fishserializer2,customerserializer3
from rest_framework.generics import ListAPIView, CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from django.contrib.auth import authenticate




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

#ehehfffhe

class retailerslist2(ListAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer
    
    def get_queryset(self):
        user= self.request.user
        return retailers.objects.filter(fish1__name='mardine')


class retailerslist3(ListAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer
    
    def get_queryset(self):
        user= self.request.user
        return retailers.objects.filter(fish1__name='mardine')


class retailerslist3(ListAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer
    
    def get_queryset(self):
        user= self.request.user
        return retailers.objects.filter(fish1__name='mardine')

#rhrhrhrhr

class fishermanlist2(ListAPIView):
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer
    
    def get_queryset(self):
        user= self.request.user
        return fishermen.objects.filter(fish1__name='mardine')


class fishermanlist3(ListAPIView):
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer
    
    def get_queryset(self):
        user= self.request.user
        return fishermen.objects.filter(fish1__name='mardine')



class fishermanlist4(ListAPIView):
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer
    
    def get_queryset(self):
        user= self.request.user
        return fishermen.objects.filter(fish1__name='mardine')



class fishlist(ListAPIView):
    queryset = fish1.objects.all()
    serializer_class = fishserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['retailers', 'fishermen']

#  creating

class customercreate(CreateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerserializer

class retailerscreate(CreateAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer

class fishermancreate(CreateAPIView):
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer

class fishcreate(CreateAPIView):
    queryset = fish1.objects.all()
    serializer_class = fishserializer

# delete

class deletecustomer(DestroyAPIView):
    queryset = customer.objects.all()
    serializer_class = customerserializer
   
class deletefisherman(DestroyAPIView):
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer

class deleteretailers(DestroyAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer

class deletefish(DestroyAPIView):
    queryset = fish1.objects.all()
    serializer_class = fishserializer


# update

class updatecustomer(UpdateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerserializer

class updatefisherman(UpdateAPIView):
    queryset = fishermen.objects.all
    serializer_class = fishermanserializer

class updateretailers(UpdateAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer

class updatefish(UpdateAPIView):
    queryset = fish1.objects.all()
    serializer_class = fishserializer

# retrieve

class retrievecustomer(RetrieveAPIView):
    queryset = customer.objects.all()
    serializer_class = customerserializer

class retrieveretailers(RetrieveAPIView):
    queryset = retailers.objects.all()
    serializer_class = retailerserializer

class retrievefisherman(RetrieveAPIView):
    queryset = fishermen.objects.all
    serializer_class = fishermanserializer

class retrievefish(RetrieveAPIView):
    queryset = fish1.objects.all()
    serializer_class = fishserializer


