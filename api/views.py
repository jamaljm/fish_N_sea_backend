

# Create your views here.

from .models import customer, retailers, fishermen, fish1, fish2,fishcount
from .serializers import customerserializer, retailerserializer, fishermanserializer, fishserializer, fishserializer2,fishcountserializer
from rest_framework.generics import ListAPIView, CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import generics
from django.http import response
from rest_framework.decorators import api_view

from rest_framework import status


from rest_framework.response import Response

from rest_framework import mixins


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

class fishcreate4(CreateAPIView):
    queryset = fishcount.objects.all()
    serializer_class = fishcountserializer

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
    queryset = fishermen.objects.all()
    serializer_class = fishermanserializer

class retrievefish(RetrieveAPIView):
    queryset = fish1.objects.all()
    serializer_class = fishserializer


#custom

# class fishcount(mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = fishcount.objects.filter(name='mardine')
#     serializer_class = fishcountserializer
#     lookup_field=None
    
    
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.count += 1
#         instance.save()
#         return Response({"success": True})


# class fishcount(viewsets.ViewSet):
#     def update(self, request):
        
#         # Get the object you want to update
#         obj = fishcount.objects.filter(name="mardine")
#         # Increment the field
#         obj.rating += 1
#         # Save the changes to the database
#         obj.save()
#         # Return a response
#         return Response({"success": True})

# class fishcount(generics.UpdateAPIView):
#     queryset = fishcount.objects.all()
#     serializer_class = fishcountserializer
    

    
#     def update(self, request, *args, **kwargs):
#         instance = self.filter_queryset(name='salmon')
#         instance.count += 1
#         instance.save()
#         return Response({"success": True})
    

# @api_view(['PATCH', 'PUT'])
# def update_my_model(request, name):
#     try:
#         # Retrieve the object to be updated using the name field as the primary key
#         obj = fishcount.objects.get(name=name)
#         obj.count += 1
#     except fishcount.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # Deserialize the request data using the serializer
#     serializer = fishcountserializer(obj, data=request.data, partial=True)
#     if serializer.is_valid():
#         # Save the updated object and return a success response
    
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


