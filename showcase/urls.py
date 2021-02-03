from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(), name='index'),
    path('brands/<slug:slug>/', views.BrandDetail.as_view(), name='brand_detail'),
    path('phones/<slug:slug>/', views.PhoneDetail.as_view(), name='phone_detail'),
    path('create_phone/', views.PhoneCreate.as_view(), name='create_phone'),
    path('create_brand/', views.BrandCreate.as_view(), name='create_brand'),
    path('search/', views.Search.as_view(), name='search'),
    path('phones', views.PhonesList.as_view(), name='phones')
    
]