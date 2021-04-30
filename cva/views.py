from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactdata = contact(name= name,email = email,subject = subject,message = message)
        contactdata.save()
    return render(request, 'index.html')
