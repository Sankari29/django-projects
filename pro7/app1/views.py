from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Stable

# Create your views here.
def home(request):
    return render(request,'home.html')

def reg(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        clas = request.POST.get('clas')
        Stable.objects.create(name = name, age = age, phone = phone, clas = clas)
        return redirect('home')
    return render(request,'reg.html')


def view(request):
    data = Stable.objects.all()
    return render(request,'view.html',{'data':data})


def get(request):
    if request.method == 'POST':
        data = Stable.objects.filter(id = request.POST.get('id'))
        return render(request,'view.html',{'data':data})
    return render(request,'get.html')



def edit(request):      
    if request.method =='POST' and  request.POST.get('name'):
        id = request.POST.get('id')
        print(id,"edit")
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        clas = request.POST.get('clas')
        Stable.objects.filter(id=id).update(name = name, age = age, phone = phone, clas = clas)
        return redirect('home')

    if request.method =='POST':
        data = Stable.objects.filter(id = request.POST.get('id'))
        if data:
            return render(request,'reg.html',{'data':data[0]})
        else:
            return HttpResponse('<h1> ID is Not present</h1>')
    return render(request,'edit.html')



def delete(request):
    if request.method =='POST':
        Stable.objects.get(id=request.POST.get('id')).delete()
        return redirect('home')
       
    return render(request,'del.html')
