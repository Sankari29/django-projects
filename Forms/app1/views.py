from django.shortcuts import render,redirect
from app1.forms import Reg_forms

def home(request):
    return render(request,'home.html')

# def reg(request):
    # forms=Reg_forms()
    # if request.method=='POST':
    #     fname=request.POST.get('fname')
    #     lname=request.POST.get('lname')
    #     age=request.POST.get('age')
    #     gender=request.POST.get('gender')
    #     Reg.objects.create(fname=fname,lname=lname,age=age,gender=gender)
    #     return redirect('home')
    # return render(request,'reg_forms.html',{'forms':forms})
    
def reg(request):
    var=Reg_forms()
    if request.method=='POST':
        var=Reg_forms(request.POST)
        if var.is_valid():#check values present or not
            # print(var.cleaned_data)
            # fname=var.cleaned_data('fname')
            # lname=var.cleaned_data('lname')
            # age=var.cleaned_data('age')
            # gender=var.cleaned_data('gender')
            # Reg.objects.create(fname=fname,lname=lname,age=age,gender=gender)
            var.save()
            return redirect('home')
    return render(request,'reg_forms.html',{'forms':var})