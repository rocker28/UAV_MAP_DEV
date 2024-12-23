from django.shortcuts import render


# Create your views here.


def home_page(request):
    return render(request,'base_app/homepage.html')

def about_us(request):
    return render(request, 'about-us.html')