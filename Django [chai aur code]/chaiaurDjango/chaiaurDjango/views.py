from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

'''
def home(request):
    return HttpResponse("Hello it's a Home Page")

def about(request):
    return HttpResponse("Hello  it's a About page")

def contact(request):
    return HttpResponse("Contact me i email/whatsapp")
    '''