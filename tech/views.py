from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tech_pg(request):
        return render(request, 'tech/tech.html')