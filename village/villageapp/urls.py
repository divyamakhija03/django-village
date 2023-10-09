from django.urls import path
from . import views



urlpatterns = [
    path('home/',views.home,name='home'),
    path('womenwelfare/',views.womenwelfare,name='womenwelfare'),
    path('appointmentcontact/', views.appointmentcontact, name='appointmentcontact'),
    path('grievance/',views.grievance,name='grievance'),
    path('savegrievance/',views.savegrievance,name='savegrievance'),
    path('utility/',views.utility,name='utility'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),


    
]