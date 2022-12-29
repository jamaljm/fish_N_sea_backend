from . import views
from django.urls import path


urlpatterns = [     
    path('customer/', views.customer_list),
    path('customer/<int:pk>/', views.customer_detail),
    path('retailers/', views.retailers_list),
    path('retailers/<int:pk>/', views.retailers_detail),
    path('fishermen/', views.fishermen_list),
    path('fishermen/<int:pk>/', views.fishermen_detail),
    path('fish1/', views.fish1_list),
    path('fish1/<int:pk>/', views.fish1_detail),
    path('fish2/', views.fish2_list),
    path('fish2/<int:pk>/', views.fish2_detail),
]
