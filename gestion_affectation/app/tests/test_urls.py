from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import (
    home,
    employe,
    lieu,
    affecter,
)

class URLTest(SimpleTestCase):
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, home.login)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home.index)

    def test_employes_url_resolves(self):
        url = reverse('employes')
        self.assertEqual(resolve(url).func, employe.employes)

    def test_add_employes_url_resolves(self):
        url = reverse('add_employes')
        self.assertEqual(resolve(url).func, employe.addEmploye)

    def test_update_employes_url_resolves(self):
        url = reverse('update_employes', args=[1])  # Replace 1 with the actual ID
        self.assertEqual(resolve(url).func, employe.updateEmploye)

    def test_delete_employes_url_resolves(self):
        url = reverse('delete_employes', args=[1])  # Replace 1 with the actual ID
        self.assertEqual(resolve(url).func, employe.deleteEmploye)

    def test_lieux_url_resolves(self):
        url = reverse('lieux')
        self.assertEqual(resolve(url).func, lieu.lieux)

    def test_add_lieux_url_resolves(self):
        url = reverse('add_lieux')
        self.assertEqual(resolve(url).func, lieu.addLieu)

    def test_update_lieux_url_resolves(self):
        url = reverse('update_lieux', args=[1])  # Replace 1 with the actual ID
        self.assertEqual(resolve(url).func, lieu.updateLieu)

    def test_delete_lieux_url_resolves(self):
        url = reverse('delete_lieux', args=[1])  # Replace 1 with the actual ID
        self.assertEqual(resolve(url).func, lieu.deleteLieu)

    def test_affectations_url_resolves(self):
        url = reverse('affectations')
        self.assertEqual(resolve(url).func, affecter.affecters)

    def test_add_affecter_url_resolves(self):
        url = reverse('add_affecter')
        self.assertEqual(resolve(url).func, affecter.addAffecter)

    def test_update_affecter_url_resolves(self):
        url = reverse('update_affecter', args=[1])  # Replace 1 with the actual ID
        self.assertEqual(resolve(url).func, affecter.updateAffecter)

    def test_delete_affecter_url_resolves(self):
        url = reverse('delete_affecter', args=[1])  # Replace 1 with the actual ID
        self.assertEqual(resolve(url).func, affecter.deleteAffecter) 