from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SignUpForm
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

