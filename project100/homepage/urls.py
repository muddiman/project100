from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login') 
]