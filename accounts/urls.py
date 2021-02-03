from django.urls import path
from . import views 

urlpatterns = [
    path('sign_up/',views.SignUp.as_view(), name='sign_up'),
    path('login/', views.SignIn.as_view(), name='sign_in'),
    path('logout/', views.Exit.as_view(), name='log_out')
]