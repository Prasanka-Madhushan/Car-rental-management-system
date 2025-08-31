import email
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from .models import usertable, booking_table, vehicle_table, contactus, feedback
import random
from django.views import View
from .process import html_to_pdf
from django.template.loader import render_to_string
from django.views.generic import View
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.conf import settings

from .models import PasswordResetToken

def index(request):
    fetchvehicle = vehicle_table.objects.all()
    
    # if (request.session["log_id"]<=0):
    #     id = request.session["log_id"]
    #     # udata = usertable.objects.filter(id=id)[0]
    
    # else:
    #     print(id)

    # logid = request.session['log_id']
    # userdata = usertable.objects.filter(id=logid)[0]
    userdata = usertable.objects.all() 
    try:
        print(request.session["log_id"])
        user=usertable.objects.filter(id=request.session["log_id"])[0]
    except:
         user=None
    ## This is for random Vehicle values#
    x=list(vehicle_table.objects.all())
    x=random.sample(x, 9)
    print(userdata)
    # print(fname)

    return render(request, "index.html", {"vehicle": fetchvehicle, "x":x, "userdata":userdata,"user":user})

    
    # return render(request, 'index.html', {'udata':udata})


def termsandconpage(request):
    return render(request, "termsandconpage.html")


# @login_required
def checkout(request, id):
    fetch = vehicle_table.objects.get(id=id)
    print(id)
    print(fetch)
    return render(request, "checkout.html", {"vehicle": fetch})


def checkoutform(request):
    return render(request, "checkoutform.html")


def services(request):
    return render(request, "services.html")


# def loginform(request):
#     return render(request,'loginform.html')
#
# def loginform2(request):
#     return render(request,'loginform2.html')


def vehicles(request):
    fetchvehicle = vehicle_table.objects.all()
    ## This is for random vehicle values
    x=list(vehicle_table.objects.all())
    x=random.sample(x, 9)
    return render(request, "vehicles.html", {"vehicle": fetchvehicle,"x":x})


def contact(request):
    return render(request, "contact.html")


def feedbackpage(request):
    return render(request, "feedback.html")


# @login_required()
def bookingpage(request):
    # if usertable.objects.filter(login_id=userid).exists():

    uid = request.session["log_id"]
    vdata = booking_table.objects.filter(login_id=uid)
    # data = booking_table.objects.all()
    print("uid is :", uid)
    print("This is vdata :",vdata)
    return render(request, "bookingpage.html", {"vdata": vdata})


def logout(request):
    try:
        del request.session["log_user"]
        del request.session["log_id"]
    except:
        pass
    return redirect("/index")


# login form start ------
def showdata(request):
    if request.method == "POST":

        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        password = request.POST.get("pass")
        rpassword = request.POST.get("rpass")
        phoneno = request.POST.get("phone")
        licence_no = request.POST.get("lnc_no")
        address = request.POST.get("address")

        if email == "" or fname == "" or lname == "" or password == "" or rpassword == "":
            messages.error(request, "Please Fill All Required Field.")

        elif password == rpassword:
            if password == "" and rpassword == "":
                messages.error(request, "Password and Confirm Password Field can not be empty.")

            else:
                a=usertable.objects.filter(emailid=email)
                if a:
                    messages.error(request, "This email is already registered!")
                else:

                      logindata = usertable(fname=fname, lname=lname, emailid=email, password=password, rpassword=rpassword, role=2, status=1,phonen=phoneno,licence=licence_no,addres=address)
                      logindata.save()
                      messages.success(request, "Registartion done!")
                      return redirect("index")

        else:
            messages.error(request, "Your Password and Confirm Password does not Matched!!")
            return redirect("index")
    else:
        messages.error(request, "error occured!")

    return render(request, "index.html")

    #     elif password == rpassword:
    #         if usertable.objects.filter(name=name).exists():
    #             messages.info(request, "Username Already Taken")
    #             return redirect('index')
    #         elif usertable.objects.filter(emailid=email).exists():
    #             messages.info(request, "Email Already Taken")
    #             return redirect('index')
    #         else:
    #             logindata = usertable(emailid=email, phoneno=phoneno, password=password,rpassword=rpassword, name=name, licence_no=licence_no, address=address, role=2, status=1)
    #             logindata.save()
    #             messages.success(request, 'Registartion done!')
    #             print("User Created..")
    #             return redirect('index')
    #
    #     else:
    #         messages.error(request, 'Your Password and Confirm Password does not Matched!!')
    #         return redirect('index')
    # else:
    #     messages.error(request, 'error occured!')
    #
    # return render(request, 'index.html')
def imageUpload(request):
     email=request.POST.get('email')
     print(email)
     equest_file = request.FILES['upload123'] if 'upload123' in request.FILES else None
     print(equest_file)
     file_url = None
     if equest_file:
         upload = request.FILES['upload123']
         fss = FileSystemStorage()
         file = fss.save(upload.name, upload)
         file_url = fss.url(file)
         usertable.objects.filter(emailid=email).update(image=file_url)

     
     return redirect('/myprofile')

def checklogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['upass']
        try:
            print("this is Check login try...")
            user = usertable.objects.get(emailid=email,password=password)
            print("this is Check login matched...")

            request.session['log_user'] = user.emailid
            request.session['log_id'] = user.id

            print('log_user is :',request.session['log_user'])
            print('log_id is :',request.session['log_id'])
            print('user is :',user)
            request.session.save()

        except usertable.DoesNotExist:
            
            user = None

        if user is not None:
            # messages.info(request, 'user is not None')
            # return redirect('index')
            print("user is not None!!")
            # return render(request, "index.html")
            return redirect('index')
            # return render(request,"Userprofile/myprofile.html")

        else:
            messages.info(request, 'account does not exit plz sign in')
            return redirect('index')
    return render(request,'index')

    #     if usertable.objects.filter(emailid=email).exists():
    #         if usertable.objects.filter(password=password).exists():
    #             request.session['log_user'] = email
    #             request.session['log_id'] = password
    #             request.session.save()
    #             return redirect('index')
    #
    #         else:
    #             messages.error(request,"password is Invalid. You can try again..")
    #             return redirect('index')
    #     else:
    #         messages.info(request, 'account does not exit plz sign in')
    #         return redirect('index')
    # return render(request,'index.html')


def forgotPswd(request):
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            # Generate token
            token = get_random_string(32)
            PasswordResetToken.objects.create(user=user, token=token)
            reset_link = request.build_absolute_uri(reverse('resetPswd', args=[token]))
            # Send email
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            message = "A password reset link has been sent to your email."
        except User.DoesNotExist:
            message = "No user found with this email."
    return render(request, 'forgotPswd.html', {'message': message})

def reset_password(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token)
    except PasswordResetToken.DoesNotExist:
        return render(request, 'resetPswd.html', {'error': 'Invalid or expired token.'})

    if request.method == "POST":
        password = request.POST.get("password")
        user = reset_token.user
        user.set_password(password)
        user.save()
        reset_token.delete()
        return render(request, 'resetPswd.html', {'success': 'Password reset successful!'})
    return render(request, 'resetPswd.html', {'token': token})

# login form end ------

# contact form start -----


def contactdata(request):
    if request.method == "POST":

        name = request.POST.get("fname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("mess")

        logindata = contactus(email=email, phone=phone, message=message, name=name, contact_date="no")
        logindata.save()
        messages.success(request, "Data has been submitted")
    else:
        messages.error(request, "error occurred!")

    return render(request, "index.html")


# contact form end --------


def feedbackshow(request):
    if 'log_id' not in request.session:
                messages.success(request, "please login first!")
                return redirect('/index')
    if request.method == "POST":

        name = request.POST.get("name")
        comments = request.POST.get("comments")
        ratings = request.POST.get("rating1")
        uid = request.session["log_id"]
        print("this is name :",name)
        print("this is uid :",uid)
        feedbackdata = feedback.objects.create(name=name, comments=comments, l_id=usertable(id=uid), ratings=ratings)
        feedbackdata.save()
        print("this is feedback :",uid)
        messages.success(request, "Data has been submitted!")
    else:
        messages.error(request, "error occured!")

    return render(request, "index.html")


def bookingshow(request):
    if request.method == "POST":

        
        from_duration = request.POST.get("sdate")
        to_duration = request.POST.get("edate")
        
        vid = request.POST.get("vid")
        dollar = request.POST.get("dollar")
        if 'log_id' not in request.session:
                messages.success(request, "please login first!")
                return redirect('/index')
        uid = request.session["log_id"]
        from datetime import datetime
        date_format = "%Y-%m-%d"
        a1= datetime.now() 
              
        a = datetime.strptime(str(from_duration), date_format)
        b = datetime.strptime(str(to_duration), date_format)
        print(a)
        print(b)
        if a1<a:

                if b > a:
                    delta = b - a
                    print(delta.days)
        
                    dayss = int(delta.days)
                    amount = dayss * int(dollar)
                    print(amount)
        
                    bookingdata = booking_table(amount=amount, from_to=to_duration, from_duration=from_duration, login_id=usertable(id=uid), vehicle_id=vehicle_table(id=vid), status=True)
                    print("this is Booking data after save :",bookingdata)
                    bookingdata.save()
                    print("this is Booking data before save :",bookingdata)
                    messages.success(request, "Booking Done!")
                elif a > b:
                    messages.error(request, "Please Enter a Valid Date Formate!!!")
                    return redirect("index")
        
                else: 
                    # fetch = vehicle_table.objects.get(vid=vid)
                    messages.error(request, "Please Enter a Valid Date Formate!!!")
                    return redirect("index")
        else:
                    messages.error(request, "Please Enter a Valid Date Formate!!!")
                    return redirect("index")
            # return redirect("/checkout/<int:id>")
            # fetch = vehicle_table.objects.get(id=vid)
            # return redirect('/checkout/<vid>')
            # return redirect('/checkout/')

    else:
        messages.error(request, "error occured!")
        print("error")

    return redirect("/bookingpage")


# Cancel Booking




# myprofile
def myprofile(request):
    # logid = request.session["log_user"]
    print("this is start !!")
    print(request.session["log_user"])
    print(request.session["log_id"])
    print("this is end !!")

    loguser = request.session['log_user']
    logid = request.session['log_id']
    userdata = usertable.objects.filter(id=logid)[0]
    # user=usertable.objects.all()
    # data = usertable.objects.get(emailid=logid)
    # user = usertable.objects.get(emailid=loguser,id=logid)
    # print(user)
    print(userdata)
    print(userdata.fname)
    print(userdata.emailid)
    print(userdata.image)

    return render(request, "Userprofile/myprofile.html",{"userdata":userdata})


def inbox(request):
    data = usertable.objects.all()
    # print(data)
    return render(request, "Userprofile/inbox.html")


def helps(request):
    return render(request, "Userprofile/helps.html")


def settings(request):
    return render(request, "Userprofile/settings.html")

class invoice(View):
    def get(self, request, *args, **kwargs):
        totalOfferPrice = 0
        totalPrice = 0
        u2 = usertable.objects.get(emailid=request.session['log_user'])
        u1 = u2.id
        od1 = booking_table.objects.filter(id=self.kwargs['t_no'],login_id=u1)
        u3=od1[0].vehicle_id
        
        o1 = vehicle_table.objects.filter(vehicle_name=u3)[0]
        
        
        
        
        data = {
            'order':o1,
            'orderDetails':od1,
            'user':u2,
            'totalPrice':totalPrice
        }
        open('rentalapp/templates/temp.html',"w").write(render_to_string("invoice.html",{"data":data}))

        pdf = html_to_pdf('temp.html')

        return HttpResponse(pdf,content_type='application/pdf')
class cancel(View):
    def get(self, request, *args, **kwargs):
          booking_table.objects.filter(id=self.kwargs['t_no']).update(status=False)
          return redirect('/bookingpage')