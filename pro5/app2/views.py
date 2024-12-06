from django.shortcuts import render

def home(request):
    return HttpResponse('<h1> App2 Home page </h1>')

def about(request):
    return HttpResponse('<h1> App2 About page </h1>')