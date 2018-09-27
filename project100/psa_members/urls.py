from django.urls import path
from . import views

urlpatterns = [
    path('', views.psa_members_list, name='psa_members_list')
]
 