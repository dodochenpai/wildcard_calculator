from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'password1':
            return HttpResponse('Successful Login')
        else:
            return HttpResponse('Unsuccessful Login')
    except:
        pass

    return render(request, 'login.html')

def login_csrf(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'password1':
            return HttpResponse('Successful Login')
        else:
            return HttpResponse('Unsuccessful Login')
    except:
        pass

    return render(request, 'login_csrf.html')