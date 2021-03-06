from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="About Us"),
    path('contact/', views.contact, name="Contact us"),
    path('tracker/', views.tracker, name="Tracking Status"),
    path('search/', views.search, name="Search"),
    path('products/<int:myid>', views.productview, name="Productview"),
    path('checkout/', views.checkout, name="Checkout"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
]