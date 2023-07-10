from django.shortcuts import render, redirect
from app.forms.affecter import AffecterForm
from app.models import Affecter, Lieu, Employe
from app.views import errors 
from django.db import connection
# import datetime
# cursor = connection.cursor()


#========== LISTE DES AFFECTER =============#
def affecters(response):
    employes =  Employe.objects.all()
    lieux = Lieu.objects.all()
    affecters = Affecter.objects.select_related('employe').select_related('lieu').all()
    data = {"title": "AFFECTER", "affecters": affecters, 'employes': employes, 'lieux': lieux}
    return render(response, "affecter.html", data)

	#========== ADD AFFECTER ====================#
def addAffecter(request):
	if request.method == 'POST':
		form = AffecterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/bda/gestion_affectation/affectations/')
		else:
			return errors.server_error(request, "Erreur inattendu du serveur, Echec de l'enregistrement")
	else:
		return errors.server_error(request, "Cette page n'est pas accessible avec la methode 'GET'!")

#============ UPDATE EMPLOYE ===============#
def updateAffecter(request, id_affecter):
	if request.method == 'POST':
		affecter = Affecter.objects.get(id_affecter=id_affecter)
		form = request.POST
		affecter.employe = Employe.objects.get(id_employe=int(form['up_id_employe']))
		affecter.lieu = Lieu.objects.get(id_lieu=int(form['up_id_lieu']))
		affecter.date = form['up_date']
		affecter.save()
		# format = '%Y-%m-%d'
		# date = datetime.datetime.strptime(form['up_date'], format).date()
		# cursor.execute(f"UPDATE AFFECTER SET date={date} WHERE id_affecter={id_affecter}")

		return redirect('/bda/gestion_affectation/affectations/')
	else:
		return errors.server_error(request, "Cette page n'est pas accessible avec la methode 'GET'!")

#============ DELETE EMPLOYE ================#
def deleteAffecter(request, id_affecter):
	affecter = Affecter.objects.get(id_affecter=id_affecter)
	affecter.delete()
	return redirect('/bda/gestion_affectation/affectations/')