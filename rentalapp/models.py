from django.db import models
from django.utils.safestring import mark_safe
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usertable(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    emailid = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    rpassword = models.CharField(max_length=30, blank=True,null=True)
    phonen= models.CharField(max_length=13,default="123")
    licence = models.CharField(max_length=50,default="123")
    addres = models.CharField(max_length=500,default="Doest Have")
    image= models.CharField(max_length=60,default="/media/hello.jpg")
    role = models.CharField(max_length=30)
    status = models.CharField(max_length=30)


    def __str__(self):
        return self.emailid
        return self.name

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class vehicle_table(models.Model):
    vehicle_name = models.CharField(max_length=40)
    vehicle_color = models.CharField(max_length=40)
    vehicle_number = models.CharField(max_length=40)
    vehicle_type = models.CharField(max_length=40)
    vehicle_location = models.CharField(default="None",max_length=20)
    rent_per_day = models.CharField(max_length=40)
    vehicle_photo = models.ImageField(upload_to='photos')
    vehicle_description = models.TextField()

    def vehicle_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.vehicle_photo.url))

    vehicle_image.allow_tags = True

    def __str__(self):
        return self.vehicle_name


class booking_table(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(vehicle_table,on_delete=models.CASCADE)
    login_id = models.ForeignKey(usertable,on_delete=models.CASCADE)
    from_duration = models.DateField(blank=False, null=False)
    from_to = models.DateField(blank=False, null=False)
    amount = models.CharField(max_length=30)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __int__(self):
        self.vehicle_id
        self.booking_date

class feedback(models.Model):
    l_id = models.ForeignKey(usertable,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    ratings = models.CharField(max_length=25)
    comments = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    message = models.CharField(max_length=30)
    contact_date = models.DateTimeField(auto_now_add=True , editable=False)

    def __str__(self):
        return self.name
    


