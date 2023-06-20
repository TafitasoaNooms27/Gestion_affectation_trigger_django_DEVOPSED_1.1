from django.shortcuts import render, redirect
from app.forms.lieu import LieuForm
from app.models import Lieu
from app.views import errors 

#========== LISTE DES EMPLOYES =============#
def lieux(response):
	lieux = Lieu.objects.all()
	data = {"title": "LIEUX", "lieux": lieux}
	return render(response, "lieu.html", data)

	#========== ADD EMPLOYES ====================#
def addLieu(request):
	if request.method == 'POST':
		form = LieuForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bda/gestion_affectation/lieux/')
		else:
			return errors.server_error(request, "Erreur inattendu du serveur, Echec de l'enregistrement")
	else:
		return errors.server_error(request, "Cette page n'est pas accessible avec la methode 'GET'!")

#============ UPDATE EMPLOYE ===============#
def updateLieu(request, id_lieu):
	if request.method == 'POST':
		lieu = Lieu.objects.get(id_lieu=id_lieu)
		form = LieuForm(request.POST, instance=lieu)
		if form.is_valid():
			form.save()
			return redirect('/bda/gestion_affectation/lieux/')
		else:
			return errors.server_error(request, "Erreur inattendu du serveur, Echec de l'enregistrement")
	else:
		return errors.server_error(request, "Cette page n'est pas accessible avec la methode 'GET'!")
#============ DELETE EMPLOYE ================#
def deleteLieu(request, id_lieu):
	lieu = Lieu.objects.get(id_lieu=id_lieu)
	lieu.delete()
	return redirect('/bda/gestion_affectation/lieux/')