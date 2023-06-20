from django.urls import path
from app.views import home
from app.views import employe
from app.views import lieu
from app.views import affecter

urlpatterns = [
	path('login/', home.login),
	path('home/', home.index),
	path('employes/', employe.employes, name='employes'),
	path('add_employes/', employe.addEmploye, name='add_employes'),
	path('update_employes/<id_employe>/', employe.updateEmploye),
	path('delete_employes/<id_employe>/', employe.deleteEmploye),
	path('lieux/', lieu.lieux, name='lieux'),
	path('add_lieux/', lieu.addLieu, name='add_lieux'),
	path('update_lieux/<id_lieu>/', lieu.updateLieu),
	path('delete_lieux/<id_lieu>/', lieu.deleteLieu),
	path('affectations/', affecter.affecters, name='affectations'),
	path('add_affectations/', affecter.addAffecter, name='add_affecter'),
	path('update_affectations/<id_affecter>/', affecter.updateAffecter),
	path('delete_affectations/<id_affecter>/', affecter.deleteAffecter),
]