from django.db import models

# Create your models here.
class especialidad(models.Model):
    espe_codigo = models.AutoField(primary_key=True)
    espe_descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20)
    def __unicode__(self):
        return self.espe_descripcion
    class META:
        verbose_name_plural = "Especialidades"

class area(models.Model):
    id_area = models.AutoField(primary_key=True)
    area = models.CharField(max_length=250)
    funcion = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    def __unicode__(self):
        return self.area
    class META:
        verbose_name_plural = "Areas"


class amca(models.Model):
    amca_cod = models.AutoField(primary_key=True)
    amca_desc = models.CharField(max_length=255)
    homologadocas = models.CharField(max_length=255)
    def __unicode__(self):
        return self.amca_desc

class intervencion(models.Model):
    id_intev = models.AutoField(primary_key=True)
    interv_glosa = models.CharField(max_length=255)
    grpdescripcion = models.CharField(max_length=255)
    sgrdescripcion = models.CharField(max_length=255)
    amca_cod = models.BigIntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.interv_glosa


class tipo_privilegio(models.Model):
    id_tipo_privilegio = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    def __unicode__(self):
        return self.tipo


class atributo(models.Model):
    id_atributo = models.AutoField(primary_key=True)
    atributo = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    def __unicode__(self):
        return self.atributo


class tipo_documento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    def __unicode__(self):
        return self.tipo_documento


class documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    docuemento = models.BigIntegerField(blank=True, null=True)
    tipo = models.ForeignKey(tipo_documento,blank=True, null=True)
    estado = models.CharField(max_length=255)
    rel_atributo = models.ManyToManyField(atributo,blank=True, null=True)
    def __unicode__(self):
        return self.estado


class privilegio(models.Model):
    id_privilegio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    desc_abreviada = models.CharField(max_length=255)
    tipo = models.ForeignKey(tipo_privilegio, blank=True, null=True)
    rel_area = models.ManyToManyField(area, blank=True, null=True)
    rel_amca = models.ManyToManyField(amca, blank=True, null=True)
    rel_intervenciones = models.ManyToManyField(intervencion, blank=True, null=True)
    rel_documento = models.ManyToManyField(documento, blank=True, null=True)
    rel_atributo = models.ManyToManyField(atributo, blank=True, null=True)
    rel_especialidad = models.ManyToManyField(especialidad, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion

