import qrtools
from django.conf import settings
from qrtools import QR
from models import Person
from django.db import DoesNotExist
from django.core.exceptions import ImproperlyConfigured

setting.configure()
myCode = QR()
con = True

while(con):
    try:
        Pass
    except ImproperlyConfigured:
        try:
            myCode.decode_webcam()
            data =  int(myCode.data)
            person = Person.objects.get(id=data)
            person.workshop1 = u'Done'
            person.save()
        except DoesNotExist:
            con = False
            print "Sorry! Candidte Does not exist"
    
