from django.http import HttpResponse
from django.shortcuts import render
from calculator import calculateRange
from calculator import calculateWildcard


def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == '123456':
            return HttpResponse('Successful Login')
        else:
            return HttpResponse('Unsuccessful Login')
    except:
        pass

    return render(request, 'login.html')