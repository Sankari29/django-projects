def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def fibo(num):
    res=[]
    a,b,c=0,1,0
    while c < num:
        res.append(str(a))
        a,b = b,a+b
        c+=1
    return res

def even_or_odd(n):
    if n % 2 == 0:
        return f"{n} is an Even Number"
    else:
        return f"{n} is an Odd Number"

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

def is_palindrome(s):
    return s == s[::-1]