from django.shortcuts import render,HttpResponse


def home(request):
    return HttpResponse('<h1>App2 home page</h1>')

def about(request):
    return HttpResponse('<h1>This is about page</h1>')


def contact(request):
    return HttpResponse('<h1>This is contact page</h1>')


