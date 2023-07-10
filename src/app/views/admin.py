from django.shortcuts import render, redirect
from app.models import AuditEmp, AuditLieu, AuditAffecter


def audit_employe(r):
	data = {
		"title": "EMPLOYE",
		"audits" : AuditEmp.objects.all()
	}
	return render(r, 'admin/audit_employe.html', data)


def audit_lieu(r):
	data = {
		"title": "LIEU",
		"audits" : AuditLieu.objects.all()
	}
	return render(r, 'admin/audit_lieu.html', data)


def audit_affecter(r):
	data = {
		"title": "AFFECTER",
		"audits" : AuditAffecter.objects.all()
	}
	return render(r, 'admin/audit_affecter.html', data)

