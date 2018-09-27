from django.shortcuts import render

# Create your views here.

def psa_members_list(request):
    return render(request, 'psa_members/psa_members_list.html', {}) 