
from django.http import HttpResponse
from django.shortcuts import render
from calculator import calculateRange
from calculator import calculateWildcard



def calculate(request):

    try:
        addressRange = request.GET['addressRange']
        (ipAddress, wildcardMask) = calculateWildcard(addressRange)
        return render(request, 'calculator.html', {'ipAddress': ipAddress, 'wildcardMask': wildcardMask})
    except:
        pass

    try:
        networkAddress = request.GET['networkAddress']
        networkMask = request.GET['networkMask']
        print(networkAddress)
        print(networkMask)
        range = calculateRange(networkAddress, networkMask)
        print(range)
        return render(request, 'calculator.html', {'range':range})
    except:
        pass

    return render(request, 'calculator.html')

def range(request):
    addresses = request.GET['addresses']
    output = calculateRange(addresses)
    return render(request, "output.html", {'output':output})