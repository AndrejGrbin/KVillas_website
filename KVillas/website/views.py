from django.shortcuts import render

def home(request):
	return render(request, "home.html", {} )

def de_home(request):
	return render(request, "de_home.html", {} )

def villa_adora(request):
	return render(request, "villa_adora.html", {} )

def villa_amia(request):
	return render(request, "villa_amia.html", {} )

def villa_shimunelka(request):
	return render(request, "villa_shimunelka.html", {} )