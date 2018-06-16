from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def work(request):
  return render(request, 'how-it-works.html')