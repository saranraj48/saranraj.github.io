from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^megaevents', views.megaevents, name='megaevents'),
    url(r'^funbox', views.funbox, name='funbox'),
    url(r'^techeve', views.techeve, name='techeve'),
    url(r'^register', views.register, name='register'),
    url(r'^admitcard', views.admitcard, name='admitcard'),
    url(r'^sitecredits', views.sitecredits, name='sitecredits'),
    url(r'^candidates', views.candidates, name='candidates'),
    url(r'^accomodation', views.accomodation, name='accomodation'),
    url(r'^paymentview', views.paymentview, name='paymentview'),
    url(r'^onspot', views.onspot, name='onspot'),
    url(r'^online', views.online, name='online'),
    url(r'^setpaid', views.setpaid, name='setpaid'),
    url(r'^paid', views.paid, name='paid'),
]
