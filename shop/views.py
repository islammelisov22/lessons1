from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse("Hello world!")
def about(request):
    print(request)
    return HttpResponse("Привет мир")
