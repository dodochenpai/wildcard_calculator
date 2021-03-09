
from django.http import HttpResponse
from django.shortcuts import render
from calculator import calculateRange
from calculator import calculateWildcard

def home(request):
    return render(request, 'calculator.html')

def wildcard(request):
    addresses = request.GET['addresses']
    output = calculateWildcard(addresses)
    return render(request, "output.html", {'output':output})

def range(request):
    addresses = request.GET['addresses']
    output = calculateRange(addresses)
    return render(request, "output.html", {'output':output})