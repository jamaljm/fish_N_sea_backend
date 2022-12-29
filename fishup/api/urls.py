from . import views
from django.urls import path


urlpatterns = [     
    
    path("signup-customer/",views.customercreate(),name="signup-owner"),
    path("signup-fisherman/",views.fishermancreate(),name="signup-fisherman"),
    path("signup-retailer/",views.retailerscreate(),name="signup-retailer"),
    path("addfish/",views.fishcreate(),name="addfish"),
    path("listfish/",views.fishlist(),name="listfish"),
    path("listcustomer/",views.customerlist(),name="listcustomer"),
    path("listretailer/",views.retailerslist(),name="listretailer"),
    path("listfisherman/",views.fishermanlist(),name="listfisherman"),
    

    



]