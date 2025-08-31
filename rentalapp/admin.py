from django.contrib import admin
from .models import usertable , vehicle_table , booking_table , feedback ,contactus

# Register your models here.

class showuser(admin.ModelAdmin):
    list_display = ['fname','lname','emailid','password', 'rpassword','role','status','phonen','licence','addres']

admin.site.register(usertable,showuser)


class showvehicle(admin.ModelAdmin):
    list_display = ['vehicle_name', 'vehicle_color', 'vehicle_number', 'vehicle_type', 'vehicle_image', 'vehicle_description', 'rent_per_day','vehicle_location']

admin.site.register(vehicle_table, showvehicle)

class showbookings(admin.ModelAdmin):
    list_display = ['vehicle_id', 'login_id', 'from_duration', 'from_to', 'amount', 'booking_date', 'status']


admin.site.register(booking_table, showbookings)

class showfeedback(admin.ModelAdmin):
    list_display = ['l_id','name', 'ratings', 'comments']


admin.site.register(feedback, showfeedback)

class showcontactus(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','message','contact_date']

admin.site.register(contactus, showcontactus)

