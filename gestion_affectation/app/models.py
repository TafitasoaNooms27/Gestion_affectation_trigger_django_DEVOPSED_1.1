# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Affecter(models.Model):
    id_affecter = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', models.DO_NOTHING)
    lieu = models.ForeignKey('Lieu', models.DO_NOTHING)
    date = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'AFFECTER'


class Employe(models.Model):
    id_employe = models.AutoField(primary_key=True)
    codeemp = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    poste = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'EMPLOYE'


class Lieu(models.Model):
    id_lieu = models.AutoField(primary_key=True)
    codelieu = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    province = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'LIEU'


class AuditAffecter(models.Model):
    id_audit_affecter = models.AutoField(primary_key=True)
    date_suivi = models.DateField()
    type_action = models.CharField(max_length=200)
    utilisateur = models.CharField(max_length=200)
    old_id_employe = models.IntegerField(blank=True, null=True)
    id_employe = models.IntegerField(blank=True, null=True)
    old_id_lieu = models.IntegerField(blank=True, null=True)
    id_lieu = models.IntegerField(blank=True, null=True)
    old_date = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_affecter'


class AuditEmp(models.Model):
    id_audit_employe = models.AutoField(primary_key=True)
    date_suivi = models.DateField()
    type_action = models.CharField(max_length=20)
    utilisateur = models.CharField(max_length=255)
    old_code_employe = models.CharField(max_length=255)
    code_employe = models.CharField(max_length=255)
    old_nom = models.CharField(max_length=255)
    nomemp = models.CharField(max_length=255)
    old_prenom = models.CharField(max_length=255)
    prenomemp = models.CharField(max_length=255)
    old_poste = models.CharField(max_length=255, blank=True, null=True)
    posteemp = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'audit_emp'


class AuditLieu(models.Model):
    id_audit_lieu = models.AutoField(primary_key=True)
    type_action = models.CharField(max_length=255)
    date_suivi = models.DateField()
    utilisateur = models.CharField(max_length=255)
    old_code_lieu = models.CharField(max_length=255)
    code_lieu = models.CharField(max_length=255)
    old_designation = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    old_province = models.CharField(max_length=255)
    province = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'audit_lieu'
