from django.test import TestCase, Client
from django.urls import reverse
from app.models import Affecter, Employe, Lieu

class AffecterViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.lieu = Lieu.objects.create(codelieu='L001', designation='Lieu 1', province='Province 1')
        self.employe = Employe.objects.create(codeemp='E001', nom='Doe', prenom='John', poste='Developer')
        self.affecter = Affecter.objects.create(employe=self.employe, lieu=self.lieu, date='2021-01-01')
        self.affecters_url = reverse('affecters')
        self.add_affecter_url = reverse('addAffecter')
        self.update_affecter_url = reverse('updateAffecter', args=[self.affecter.id_affecter])
        self.delete_affecter_url = reverse('deleteAffecter', args=[self.affecter.id_affecter])

    def test_affecters_view(self):
        response = self.client.get(self.affecters_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'affecter.html')

    def test_add_affecter_view(self):
        data = {
            'employe': self.employe.id_employe,
            'lieu': self.lieu.id_lieu,
            'date': '2021-01-02'
        }
        response = self.client.post(self.add_affecter_url, data)
        self.assertEqual(response.status_code, 302)

    def test_update_affecter_view(self):
        data = {
            'up_id_employe': self.employe.id_employe,
            'up_id_lieu': self.lieu.id_lieu,
            'up_date': '2021-01-03'
        }
        response = self.client.post(self.update_affecter_url, data)
        self.assertEqual(response.status_code, 302)

    def test_delete_affecter_view(self):
        response = self.client.get(self.delete_affecter_url)
        self.assertEqual(response.status_code, 302)

class EmployeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.employe = Employe.objects.create(codeemp='E001', nom='Doe', prenom='John', poste='Developer')
        self.employes_url = reverse('employes')
        self.add_employe_url = reverse('addEmploye')
        self.update_employe_url = reverse('updateEmploye', args=[self.employe.id_employe])

    def test_employes_view(self):
        response = self.client.get(self.employes_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employe.html')

    def test_add_employe_view(self):
        data = {
            'codeemp': 'E002',
            'nom': 'Smith',
            'prenom': 'Jane',
            'poste': 'Manager'
        }
        response = self.client.post(self.add_employe_url, data)
        self.assertEqual(response.status_code, 302)

    def test_update_employe_view(self):
        data = {
            'codeemp': 'E001',
            'nom': 'Doe',
            'prenom': 'John',
            'poste': 'Senior Developer'
        }
        response = self.client.post(self.update_employe_url, data)
        self.assertEqual(response.status_code, 302)