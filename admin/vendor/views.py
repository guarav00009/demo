from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'vendor/vendor-registration.html')

def vendor_register(request):
    if request.method == 'POST':
        # save code to be written here
    return HttpResponse('Form Submit')
