from django.shortcuts import render,redirect
from app1.models import *

def home(request):
    return render(request,'home.html')
def profile(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mob')
        address=request.POST.get('address')
        Profile.objects.create(name=name,age=age,gender=gender,mob=mobile,address=address)
        return redirect('home')
    return render(request,'profile.html')
def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mob')
        address=request.POST.get('address')
        username=request.POST.get('user')
        password=request.POST.get('pwd')
        c_password=request.POST.get('c_pwd')
        Signup.objects.create(name=name,age=age,gender=gender,mob=mobile,address=address, user=username,password=password,c_password=c_password)
        return redirect('home')
    return render(request,'signup.html')