from django.shortcuts import render
from app1 import programs

# Create your views here.

def home(request):
    return render(request, 'home.html')

def solve(request):
    data = request.GET.get('data')  # data is a string identifying the program type
    val = request.GET.get('val')  # the input value for the program
    
    res = None  # initialize res to None by default
    
    if val:  # check if val is provided
        val_int = int(val)  # convert val to integer once, since it’s used multiple times
        
        if data == '1':  # Check if the number is prime
            res = f'{val} is a Prime Number' if programs.isprime(val_int) else f'{val} is not a Prime Number'
        
        elif data == '2':  # Generate Fibonacci sequence
            res = ' '.join(map(str, programs.fibo(val_int)))  # join elements as strings
        
        elif data == '3':  # Check if the number is even or odd
            res = f'{val} is an Even Number' if val_int % 2 == 0 else f'{val} is an Odd Number'
        
        elif data == '4':  # Check if the number is a perfect square
            res = f'{val} is a Perfect Square' if int(val_int ** 0.5) ** 2 == val_int else f'{val} is not a Perfect Square'
        
        elif data == '5':  # Check if the number is a palindrome
            res = f'{val} is a Palindrome' if val == val[::-1] else f'{val} is not a Palindrome'
    
    # Render with context including data, res, and val
    return render(request, 'solve.html', {'data': data, 'res': res, 'val': val})
