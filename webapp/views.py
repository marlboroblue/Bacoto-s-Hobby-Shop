from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, OrderForm  , LoginForm
from .models import Order
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'pages/slideshow.html')
def aboutus(request):
    return render(request, 'pages/aboutus.html')

def contactus(request):
    return render(request, 'pages/contactus.html')

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = CustomerForm()

    return render(request, 'pages/create_customer.html', {'form': form})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = OrderForm()

    return render(request, 'pages/create_order.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pages/admin.html', {'orders': orders})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin')
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})



def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = OrderForm(instance=order)

    return render(request, 'pages/update_order.html', {'form': form, 'order': order})

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('admin') 

    return render(request, 'pages/delete_order.html', {'order': order})
    

























