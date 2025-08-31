from django.urls import path
from . import views 


urlpatterns = [
    path('show_booking_table', views.show_booking_table, name='show_booking_table'),
    path('Create-Pdf',views.pdf_report_create, name='Create-Pdf'),
    path('show_vehicle_table', views.show_vehicle_table, name='show_vehicle_table'),
    path('Create-Pdf',views.pdf_report_create, name='Create-Pdf'),
    path('show_contactus', views.show_contactus, name='show_contactus'),
    path('Create-Pdf',views.pdf_report_create, name='Create-Pdf'),
    path('show_usertable', views.show_usertable, name='show_usertable'),
    path('Create-Pdf',views.pdf_report_create, name='Create-Pdf'),
    path('show_feedback', views.show_feedback, name='show_feedback'),
    path('Create-Pdf',views.pdf_report_create, name='Create-Pdf')
    
    

]