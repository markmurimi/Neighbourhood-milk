from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SignUpForm, OrderForm, LoginForm
from .models import Buyer, Order

def welcome(request):
  profiles = Buyer.get_buyers()
  return render(request, 'buyer.html', {"profiles": profiles})

def signup(request):
    '''
    View function to display a form for creating a post to a logged in authenticated user
    '''
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return render(request, 'buyer.html')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def ingia(request):
    '''
    View function to display a login form
    '''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, 'buyer.html')
    else:
        form = LoginForm()
        return render(request, 'ingia.html', {'form': form})


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, 'payment.html')
    else:
        form = OrderForm()
        return render(request, 'order.html', {'form': form})

def message(request):
    return render(request, 'feedback.html')

def payment(request):
    return render(request, 'payment.html')