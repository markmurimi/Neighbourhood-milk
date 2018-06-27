from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def work(request):
  return render(request, 'how-it-works.html')

def welcome(request):
  return render(request, 'buyer.html')

def landing(request):
  return render(request, 'landing.html')

def contact(request):
  return render(request, 'contact.html')

def  about(request):
  return render(request, 'about-us.html')