from django.shortcuts import render, redirect
from app.models import Employe, Lieu, Affecter

def login(r):
	return render(r, 'login.html')

def index(response):
	employes = Employe.objects.all();
	lieux = Lieu.objects.all();
	affecters = Affecter.objects.all();
	stats = {"count_emp": len(employes), "count_lieux": len(lieux), "count_aff": len(affecters)}
	data = {"title": "ACCUEIL", "stats": stats }
	return render(response, "home.html", data)