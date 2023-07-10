from django.test import TestCase, Client
from django.urls import reverse
from app.models import Affecter, Employe, Lieu

class AffecterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.lieu = Lieu.objects.create(codelieu='L001', designation='Lieu 1', province='Province 1')
        self.employe = Employe.objects.create(codeemp='E001', nom='Doe', prenom='John', poste='Developer')
        self.affecter = Affecter.objects.create(employe=self.employe, lieu=self.lieu, date='2021-01-01')
        self.affecter_list_url = reverse('affecters')
        self.add_affecter_url = reverse('addAffecters')
        self.update_affecter_url = reverse('updateAffecters', args=[self.affecter.id])
        self.delete_affecter_url = reverse('deleteAffecters', args=[self.affecter.id])

    def test_affecter_list_view(self):
        response = self.client.get(self.affecter_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/affecter_list.html')

    def test_add_affecter_view(self):
        response = self.client.post(self.add_affecter_url, {
            'employe': self.employe.id_employe,
            'lieu': self.lieu.id_lieu,
            'date': '2021-01-02'
        })
        self.assertEqual(response.status_code, 302)

    def test_update_affecter_view(self):
        response = self.client.post(self.update_affecter_url, {
            'employe': self.employe.id_employe,
            'lieu': self.lieu.id_lieu,
            'date': '2021-01-03'
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_affecter_view(self):
        response = self.client.post(self.delete_affecter_url)
        self.assertEqual(response.status_code, 302)