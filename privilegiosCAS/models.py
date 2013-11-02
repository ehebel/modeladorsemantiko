from django.db import models

# Create your models here.
class especialidad(models.Model):
    OPCIONES_ESTADO = ((0, 'No Vigente'),(1, 'Vigente'))
    espe_codigo = models.AutoField(primary_key=True)
    espe_descripcion = models.CharField(max_length=255)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, default=1)
    def __unicode__(self):
        return self.espe_descripcion
    class META:
        verbose_name_plural = "Especialidades"

class area(models.Model):
    OPCIONES_ESTADO = ((0, 'No Vigente'),(1, 'Vigente'))
    id_area = models.AutoField(primary_key=True)
    area = models.CharField(max_length=250)
    funcion = models.CharField(max_length=250)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, default=1)
    def __unicode__(self):
        return self.area
    class META:
        verbose_name_plural = "Areas"


class amca(models.Model):
    OPCIONES_HOMOLOGADO = ((0, 'No'),(1, 'Si'))
    amca_cod = models.AutoField(primary_key=True)
    amca_desc = models.CharField(max_length=255)
    homologadocas = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_HOMOLOGADO, default=1)
    def __unicode__(self):
        #return self.amca_desc
        return u'%s - %s' % (self.amca_cod,self.amca_desc)

class intervencion(models.Model):
    id_intev = models.CharField(max_length=20,primary_key=True)
    interv_glosa = models.CharField(max_length=255)
    grpdescripcion = models.CharField(max_length=255)
    sgrdescripcion = models.CharField(max_length=255)
    amca_cod = models.ForeignKey(amca,blank=True, null=True)
    #amca_desc = models.CharField(max_length=255)
    def __unicode__(self):
        return u'%s - %s' % (self.id_intev,self.interv_glosa)


class tipo_privilegio(models.Model):
    OPCIONES_ESTADO = ((0, 'No Vigente'),(1, 'Vigente'))
    id_tipo_privilegio = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, default=1)
    def __unicode__(self):
        return self.tipo


class atributo(models.Model):
    OPCIONES_ESTADO = ((0, 'No Vigente'),(1, 'Vigente'))
    id_atributo = models.AutoField(primary_key=True)
    atributo = models.CharField(max_length=255)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, default=1)
    def __unicode__(self):
        return self.atributo


class tipo_documento(models.Model):
    OPCIONES_ESTADO = ((0, 'No Vigente'),(1, 'Vigente'))
    id_tipo_documento = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=255)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, default=1)
    def __unicode__(self):
        return self.tipo_documento


class documento(models.Model):
    OPCIONES_ESTADO = ((0, 'No Vigente'),(1, 'Vigente'))
    id_documento = models.AutoField(primary_key=True)
    documento = models.BigIntegerField(blank=True, null=True)
    tipo = models.ForeignKey(tipo_documento,blank=True, null=True)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, default=1)
    rel_atributo = models.ManyToManyField(atributo,blank=True, null=True)
    def __unicode__(self):
        return self.estado


class privilegio(models.Model):
    OPCIONES_ESTADO = ((0, 'No Vigente'),(1, 'Vigente'))
    id_privilegio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    desc_abreviada = models.CharField(max_length=255)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, default=1)
    tipo = models.ForeignKey(tipo_privilegio, blank=True, null=True)
    rel_area = models.ManyToManyField(area, blank=True, null=True)
    rel_amca = models.ManyToManyField(amca, blank=True, null=True)
    rel_intervenciones = models.ManyToManyField(intervencion, blank=True, null=True)
    rel_documento = models.ManyToManyField(documento, blank=True, null=True)
    rel_atributo = models.ManyToManyField(atributo, blank=True, null=True)
    rel_especialidad = models.ManyToManyField(especialidad, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion

