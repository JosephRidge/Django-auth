from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('index', views.index, name='index' ),
    path('promoProducts', views.promoProducts, name='promoProducts'),
    path('login', views.loginUser, name='login'),
    path('register', views.registerUser, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('payment', views.mpesaPayment,name='mpesaPayment')

]
