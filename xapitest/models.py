from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from audit_log.models.managers import AuditLog


Group.add_to_class('menu', models.TextField())
class Archivos(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()

    audit_log = AuditLog()

    class Meta:
        permissions = (
            ("view_archivos", "Puede ver los registros"),
            ("options_archivos", "Puede ver los options"),
        )

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.titulo