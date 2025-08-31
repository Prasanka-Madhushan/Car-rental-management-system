from django.shortcuts import render
from rentalapp.models import booking_table
from rentalapp.models import vehicle_table
from rentalapp.models import contactus
from rentalapp.models import usertable
from rentalapp.models import feedback
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def show_booking_table(request):
    rentalapp = booking_table.objects.all()

    context = {

        'rentalapp' : rentalapp 
    }
    return render(request,'pdf_convert/showinfo.html', context)

def pdf_report_create(request):
    rentalapp = booking_table.objects.all()
    template_path = 'pdf_convert/pdfreport.html'
    context = {'rentalapp': rentalapp}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="booking_report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    
    
def show_vehicle_table(request):
    rentalapp = vehicle_table.objects.all()

    context = {

        'rentalapp' : rentalapp 
    }
    return render(request,'pdf_convert/vehicle.html', context)

def pdf_report_create(request):
    rentalapp = vehicle_table.objects.all()
    template_path = 'pdf_convert/pdfreportv.html'
    context = {'rentalapp': rentalapp}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="vehicle_report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    
    
def show_contactus(request):
    rentalapp = contactus.objects.all()

    context = {

        'rentalapp' : rentalapp 
    }
    return render(request,'pdf_convert/contact.html', context)

def pdf_report_create(request):
    rentalapp = contactus.objects.all()
    template_path = 'pdf_convert/pdfreportc.html'
    context = {'rentalapp': rentalapp}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="contact_report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    

def show_usertable(request):
    rentalapp = usertable.objects.all()

    context = {

        'rentalapp' : rentalapp 
    }
    return render(request,'pdf_convert/user.html', context)

def pdf_report_create(request):
    rentalapp = usertable.objects.all()
    template_path = 'pdf_convert/pdfreportu.html'
    context = {'rentalapp': rentalapp}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="booking_report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    

def show_feedback(request):
    rentalapp = feedback.objects.all()

    context = {

        'rentalapp' : rentalapp 
    }
    return render(request,'pdf_convert/feedback.html', context)

def pdf_report_create(request):
    rentalapp = feedback.objects.all()
    template_path = 'pdf_convert/pdfreportf.html'
    context = {'rentalapp': rentalapp}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="feedback_report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    
    
