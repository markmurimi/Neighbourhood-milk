from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def work(request):
  return render(request, 'how-it-works.html')

def welcome(request):
  return render(request, 'buyer.html')
