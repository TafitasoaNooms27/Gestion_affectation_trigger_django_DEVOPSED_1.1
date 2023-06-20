from django.test import TestCase
from app.forms.affecter import AffecterForm
from app.models import Affecter, Employe, Lieu

class AffecterFormTest(TestCase):
    def test_form_valid(self):
        lieu = Lieu.objects.create(codelieu='L001', designation='Lieu 1', province='Province 1')
        employe = Employe.objects.create(codeemp='E001', nom='Doe', prenom='John', poste='Developer')

        data = {
            'employe': employe.id_employe,
            'lieu': lieu.id_lieu,
            'date': '2021-01-01'
        }
        form = AffecterForm(data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        data = {
            'employe': '',
            'lieu': '',
            'date': ''
        }
        form = AffecterForm(data)
        self.assertFalse(form.is_valid())

class EmployeFormTest(TestCase):
    def test_form_valid(self):
        data = {
            'codeemp': 'E001',
            'nom': 'Doe',
            'prenom': 'John',
            'poste': 'Developer'
        }
        form = EmployeForm(data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        data = {
            'codeemp': '',
            'nom': '',
            'prenom': '',
            'poste': ''
        }
        form = EmployeForm(data)
        self.assertFalse(form.is_valid())