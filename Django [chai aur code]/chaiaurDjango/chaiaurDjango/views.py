from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello it's a Home Page")

def about(request):
    return HttpResponse("Hello  it's a About page")

def contact(request):
    return HttpResponse("Contact me i email/whatsapp")