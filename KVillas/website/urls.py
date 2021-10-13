from django.urls import path
from . import views

urlpatterns = [
	path('en', views.home, name="home"),
	path('de', views.de_home, name="de_home"),
	path('Villa_Adora/', views.villa_adora, name="villa_adora"),
	path('Villa_Amia/', views.villa_amia, name="villa_amia"),
	path('Villa_Shimunelka/', views.villa_shimunelka, name="villa_shimunelka"),
]