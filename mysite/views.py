from django.http import HttpResponse

def home(request):
    return HttpResponse("Página inicial do projeto")