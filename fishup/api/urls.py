from . import views
from django.urls import path



urlpatterns = [     
    
    path("signup-customer/",views.customercreate.as_view(),name="signup-owner"),
    path("signup-fisherman/",views.fishermancreate.as_view(),name="signup-fisherman"),
    path("signup-retailer/",views.retailerscreate.as_view(),name="signup-retailer"),
    path("addfish/",views.fishcreate.as_view(),name="addfish"),
    path("listfish/",views.fishlist.as_view(),name="listfish"),
    path("listcustomer/",views.customerlist.as_view(),name="listcustomer"),
    path("listretailer/",views.retailerslist.as_view(),name="listretailer"),
    path("listfisherman/",views.fishermanlist.as_view(),name="listfisherman"),


]