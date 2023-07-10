from django.contrib import admin

from app.models import Employe, Lieu , Affecter , AuditEmp , AuditLieu , AuditAffecter

# Register your models here.
admin.site.register(Employe)
admin.site.register(Lieu)
admin.site.register(Affecter)
admin.site.register(AuditEmp)
admin.site.register(AuditLieu)
admin.site.register(AuditAffecter)
