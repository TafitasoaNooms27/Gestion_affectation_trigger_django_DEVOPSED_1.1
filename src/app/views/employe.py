from django.shortcuts import render, redirect
from app.forms.employe import EmployeForm
from app.models import Employe
from app.views import errors 

#========== LISTE DES EMPLOYES =============#
def employes(response):
	employes = Employe.objects.all()
	data = {"title": "EMPLOYES", "employes": employes}
	return render(response, "employe.html", data)

	#========== ADD EMPLOYES ====================#
def addEmploye(request):
	if request.method == 'POST':
		form = EmployeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bda/gestion_affectation/employes/')
		else:
			return errors.server_error(request, "Erreur inattendu du serveur, Echec de l'enregistrement")
	else:
		return errors.server_error(request, "Cette page n'est pas accessible avec la methode 'GET'!")

#============ UPDATE EMPLOYE ===============#
def updateEmploye(request, id_employe):
	if request.method == 'POST':
		employe = Employe.objects.get(id_employe=id_employe)
		form = EmployeForm(request.POST, instance=employe)
		if form.is_valid():
			form.save()
			return redirect('/bda/gestion_affectation/employes/')
		else:
			return errors.server_error(request, "Erreur inattendu du serveur, Echec de l'enregistrement")
	else:
		return errors.server_error(request, "Cette page n'est pas accessible avec la methode 'GET'!")
#============ DELETE EMPLOYE ================#
def deleteEmploye(request, id_employe):
	employe = Employe.objects.get(id_employe=id_employe)
	employe.delete()
	return redirect('/bda/gestion_affectation/employes/')