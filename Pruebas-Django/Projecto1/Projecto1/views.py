from django.http import  HttpResponse

def saludar(request):
    return HttpResponse("Haciendo mi primer vista")