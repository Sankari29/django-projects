from django.http import HttpResponse

def  home(request):
    return HttpResponse('<h2>This is Project home page</h2>')