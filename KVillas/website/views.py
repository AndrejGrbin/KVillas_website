from django.shortcuts import render

def home(request):
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