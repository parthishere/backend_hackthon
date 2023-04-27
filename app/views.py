from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

# Create your views here.
@api_view(["POST"])
def register(request):
    email = request.POST.get("email")
    username = request.POST.get("name")
    
    User.objects.create(username=username, email=email)
    if email:  
        template = render_to_string('email_templates.html', {'username': username, 'email': email,
                                   })

        subject = "Registred for lakshya !"
        message = template
        email_from = "parththakkar1674@gmail.com"
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
    return Response({"ok":True})