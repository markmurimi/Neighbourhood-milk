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
    current_user = request.user

    if request.method == 'POST':

        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(buyer)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {"form": form})

def ingia(request):
    '''
    View function to display a login form
    '''
    current_user = request.user

    if request.method == 'POST':

        form = LoginForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(message)
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})

def order(request):
    '''
    View function to display a form for creating an order to a logged in authenticated user
    '''
    current_user = request.user

    if request.method == 'POST':

        form = OrderForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(message)
    else:
        form = OrderForm()
    return render(request, 'order.html', {"form": form})

def message(request):
    return render(request, 'feedback.html')
