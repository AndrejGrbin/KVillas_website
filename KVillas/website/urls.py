from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('de', views.de_home, name="de_home"),
	path('en/Villa_Adora/', views.adora, name="adora"),
	path('en/Villa_Amia/', views.amia, name="amia"),
	path('en/Villa_Shimunelka/', views.shimunelka, name="shimunelka"),
	path('de/Villa_Adora/', views.de_adora, name="de_adora"),
	path('de/Villa_Amia/', views.de_amia, name="de_amia"),
	path('de/Villa_Shimunelka/', views.de_shimunelka, name="de_shimunelka"),
]