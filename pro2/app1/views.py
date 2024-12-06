# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'programs.html')

def isprime(request):
    if request.method=='GET':
        data=request.GET.get('data')
        if data:
            num=int(data)
            for i in range(2,num):
                if num % i == 0:
                    temp='given number is not a prime number'
                    break
            else:
                temp='given number is prime number'
            return render(request,'isprime.html',{'data':temp})
    return render(request,'isprime.html')