from django.test import TestCase
from app.models import Employe, Lieu, Affecter

class EmployeModelTest(TestCase):
        employe = Employe.objects.create(codeemp='E001', nom='Doe', prenom='John', poste='Developer')
        self.assertEqual(employe.codeemp, 'E001')
        self.assertEqual(employe.nom, 'Doe')
        self.assertEqual(employe.prenom, 'John')
        self.assertEqual(employe.poste, 'Developer')

class LieuModelTest(TestCase):
    def test_create_lieu(self):
        lieu = Lieu.objects.create(codelieu='L001', designation='Bureau', province='Central')
        self.assertEqual(lieu.codelieu, 'L001')
        self.assertEqual(lieu.designation, 'Bureau')
        self.assertEqual(lieu.province, 'Central')

class AffecterModelTest(TestCase):
    def setUp(self):
        self.employe = Employe.objects.create(codeemp='E001', nom='Doe', prenom='John', poste='Developer')
        self.lieu = Lieu.objects.create(codelieu='L001', designation='Bureau', province='Central')

    def test_create_affecter(self):
        affecter = Affecter.objects.create(employe=self.employe, lieu=self.lieu, date='2023-06-03')
        self.assertEqual(affecter.employe, self.employe)
        self.assertEqual(affecter.lieu, self.lieu)
        self.assertEqual(affecter.date, '2023-06-03')