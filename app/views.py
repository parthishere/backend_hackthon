from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
@api_view(["POST"])
def register(request):
    email = request.POST.get("email")
    username = request.POST.get("name")
    phone_number = request.POST.get("phone_number")
    if email:
        template = render_to_string('email_template.html', {'username': username, 'email': email,
                                   "phonenumber":phone_number})

        subject = "Registred for FacIt !"
        message = template
        email_from = "parththakkar1674@gmail.com"
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    return Response({""})