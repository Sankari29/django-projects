from django.shortcuts import render,redirect
from app1.models import s_table


def home(request):
    return render(request,'home.html')

def reg(request):
    if request.method =='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        mob=request.POST.get('mob')
        cls_=request.POST.get('cls')
        print(name,age,mob,cls_)
        s_table.objects.create(name=name,age=age,mob=mob,clas=cls_)
        return redirect('home')
    return render(request,'reg.html')

def read_tab(request):
    table=s_table.objects.all()
    return render(request,'table.html',{'table':table})

def read(request):
    if request.method=='POST':
        mob=request.POST.get('mob')
        print(mob)
        table=s_table.objects.filter(mob=mob)
        return render(request,'table.html',{'table': table})
    return render(request,'take_data.html')
