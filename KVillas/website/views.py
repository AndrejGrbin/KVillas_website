from django.shortcuts import render
from django.core.mail import send_mail

def home(request):

	if request.method == 'POST':
		
		# do stuff with submitting the form
		message_name = request.POST['message_name']
		message_email = request.POST['message_email']
		message_villa = request.POST['message_villa']
		#message_from= request.POST['message_from']
		#message_till = request.POST['message_till']
		#message = request.POST['message']

		# Send mail
		send_mail(
			message_name, # subject
			message_villa, # message
			message_email, # from email
			['andrej.grbin@gmail.com'], # to email
			fail_silently = False,
			)

		return render(request, "home.html", {'message_name':message_name} )

	else:
		return render(request, "home.html", {} )

def de_home(request):
	return render(request, "de_home.html", {} )

def adora(request):
	return render(request, "adora.html", {} )

def amia(request):
	return render(request, "amia.html", {} )

def shimunelka(request):
	return render(request, "shimunelka.html", {} )

def de_adora(request):
	return render(request, "de_adora.html", {} )

def de_amia(request):
	return render(request, "de_amia.html", {} )

def de_shimunelka(request):
	return render(request, "de_shimunelka.html", {} )