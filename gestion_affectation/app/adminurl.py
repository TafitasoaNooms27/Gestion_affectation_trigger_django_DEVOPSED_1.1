from django.urls import path
from app.views import admin

urlpatterns = [
	path('audit_employe/', admin.audit_employe, name='audit_emp'),
	path('audit_lieu/', admin.audit_lieu, name='audit_lieu'),
	path('audit_affecter/', admin.audit_affecter, name='audit_aff')
]