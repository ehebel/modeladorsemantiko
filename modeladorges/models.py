import autocomplete_light
autocomplete_light.autodiscover()

from django.db import models

# Create your models here.
class ciediez(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descriptor = models.CharField(max_length=255)
    capitulo_num = models.CharField(max_length=10, null=True, blank=True)
    capitulo_titulo = models.CharField(max_length=255, null=True, blank=True)
    grupo = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.descriptor
    class Meta:
        ordering=['codigo']

class casprocedimiento(models.Model):
    idintervencionclinica = models.CharField('ID CAS',max_length=20, primary_key= True)
    integlosa = models.CharField(max_length=255)
    codgrupo = models.CharField(max_length=10)
    grpdescripcion = models.CharField(max_length=255)
    codsubgrupo = models.CharField(max_length=10)
    sgrdescripcion = models.CharField(max_length=255)
    inte_codigo_fonasa =  models.CharField(max_length=10)
    estado = models.CharField(max_length=20)
    fecha = models.DateField()
    usuario_crea = models.CharField(max_length=40)
    usuario_modif = models.CharField(max_length=40)
    def __unicode__(self):
        return self.integlosa
    class Meta:
        ordering=['idintervencionclinica']

class casdiagnostico(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20)
    fecha = models.DateField()
    usuario_crea = models.CharField(max_length=40)
    usuario_modif = models.CharField(max_length=40, null=True, blank=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering = ['codigo']

class ges_patologia(models.Model):
    id = models.IntegerField(primary_key=True)
    glosa = models.CharField(max_length=255)
    glosa_abrev = models.CharField(max_length=255, blank=True, help_text='Glosa Abreviada', verbose_name='Glosa Abreviada')
    ciediez = models.ManyToManyField('modeladorges.ciediez', blank=True, related_name="diagnostico")
    casproc = models.ManyToManyField('modeladorges.casprocedimiento', blank=True)
    casdiag = models.ManyToManyField('modeladorges.casdiagnostico', blank=True)
    def __unicode__(self):
        return self.glosa
    class Meta:
        ordering = ['id']


