from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.db import IntegrityError

from .models import Person
# Create your views here.

def index(request):
    return render(request, 'index.html')

def megaevents(request):
    return render(request, 'megaevents.html')

def techeve(request):
    return render(request, 'techeve.html')

def funbox(request):
    return render(request, 'funbox.html')

def register(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            college = request.POST.get('college','')
            accomodation = request.POST.get('accomodation','')
            department = request.POST.get('department','')
            person = Person.objects.create(candidate=name, mailid=email, college=college, accomodation=accomodation, department=department)
            person.save()
            return render(request, "registersuccess.html")
    except IntegrityError:
        message = "Sorry! The email you have entered is already Registered"
        return render(request, "register.html", {"message": message}) 
    return render(request, "register.html")

def admitcard(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email','')
            person = Person.objects.get(mailid=unicode(email))            
            return render(request, 'admitcard.html', {'person':person})
    except Person.DoesNotExist:
        message = "Sorry! The email you have entered is not Registered. Please Register!"
        return render(request, "register.html", {"message": message})
    return render(request, "register.html")

def sitecredits(request):
    return render(request, 'sitecredits.html')

def candidates(request):
    persons = []
    persons = Person.objects.all()
    return render(request, 'candidates.html', {'persons':persons})

def accomodation(request):
    persons = []
    persons = Person.objects.all()
    return render(request, 'accomodation.html', {'persons':persons})

def paymentview(request):
    persons = []
    persons = Person.objects.all()
    return render(request, 'paymentview.html', {'persons':persons})

def paid(request):
    persons = []
    persons = Person.objects.all()
    return render(request, 'paid.html', {'persons':persons})

def onspot(request):
    try:
        if request.method == "POST":
            uid = request.POST.get('id','')
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            college = request.POST.get('college','')
            phone = request.POST.get('phone','')
            accomodation = request.POST.get('accomodation','')
            department = request.POST.get('department','')
            person = Person.objects.create(id=uid, candidate=name, mailid=email, college=college, accomodation=accomodation, department=department, phone=phone)
            person.save()
            message ="Registration Sucessful"
            return render(request, "onspot.html", {"message": message})
    except IntegrityError:
        message = "Sorry! Cann't register!"
        return render(request, "onspot.html", {"message": message}) 
    return render(request, "onspot.html")

def online(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email','')
            phone = request.POST.get('phone','')
            accomodation = request.POST.get('accomodation','')
            payment = u'paid'
            person = Person.objects.get(mailid=email)
            person.phone = phone
            person.payment = payment
            person.accomodation = accomodation
            person.save()
            message ="Update Sucessful"
            return render(request, "online.html", {"message": message})
    except DoesNotExist:
        message = "Sorry! Cann't Update! Candidate does not exist!"
        return render(request, "online.html", {"message": message}) 
    return render(request, "online.html")

def setpaid(request):
    try:
        if request.method == "POST":
            id = request.POST.get('id','')
            payment = u'paid'
            person = Person.objects.get(id=id)
            person.payment = payment
            person.save()
            message ="Update Sucessful"
            return render(request, "setpaid.html", {"message": message})
    except DoesNotExist:
        message = "Sorry! Cann't Update! Candidate does not exist!"
        return render(request, "setpaid.html", {"message": message}) 
    return render(request, "setpaid.html")
