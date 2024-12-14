# views.py
from django.shortcuts import render, redirect
from .forms import CustomerForm, ProductForm
from .models import Customer, Product

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'cust.html', {'form': form})

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})


def data(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    context = {
        'customers': customers,
        'products': products
    }
    return render(request, 'data.html', context)
