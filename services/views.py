from django.shortcuts import render
from .forms import service_form
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# Create your views here.
def service_req_form(request):
    form= service_form()
    if request.method == 'POST':
        form= service_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'A SERVICE REQUEST HAS BEEN SUCESSFULLY SUBMITTED')
            return HttpResponseRedirect('/services/')
        else:
            messages.error(request, f'A SERVICE REQUEST HAS BEEN NOT SUCESSFULLY SUBMITTED: ENTER VALID DATA')
            return render(request,'services/services.html',{'form':form})

    return render(request,'services/services.html',{'form':form})
