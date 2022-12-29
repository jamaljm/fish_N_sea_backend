

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import customer, retailers, fishermen, fish1, fish2
from .serializers import customerserializer, retailerserializer, fishermanserializer, fishserializer, fishserializer2,customerserializer3
from rest_framework.generics import ListAPIView, CreateAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework.response import Response




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


# login

# class logincustomer(generics.CreateAPIView):
#     serializer_class = customerserializer3

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email","")
#         password = request.data.get("password","")
#         print(email)
#         print(password)
#         vemail=cu
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             print("heheheh")
#             serializer = customerserializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid login credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# class loginfisherman(generics.CreateAPIView):
#     serializer_class = fishermanserializer

#     def post(self, request, *args, **kwargs):
#         username = request.data.get("username", "")
#         password = request.data.get("password", "")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             serializer = fishermanserializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid login credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# class loginretailers(generics.CreateAPIView):
#     serializer_class = retailerserializer

#     def post(self, request, *args, **kwargs):
#         username = request.data.get("email", "")
#         password = request.data.get("password", "")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             serializer = retailerserializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid login credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# def login(request):
#     if method=='POST':
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             serializer = retailerserializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid login credentials"}, status=status.HTTP_401_UNAUTHORIZED)


