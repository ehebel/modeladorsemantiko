import autocomplete_light
autocomplete_light.autodiscover()

from django.db import models

class oms2008ciediez(models.Model):
    codigo = models.CharField(unique=True, max_length=20)
    descriptor = models.CharField(max_length=255)
    cod_sec = models.CharField(max_length=5,blank=True,null=True)
    cod_adicional = models.CharField(max_length=5,blank=True,null=True)
    sexo = models.PositiveIntegerField(blank=True,null=True)
    area = models.CharField(max_length=5,blank=True,null=True)
    clasificacion = models.CharField(max_length=5,blank=True,null=True)
    def __unicode__(self):
        return "%s | %s" % (self.codigo, self.descriptor)
    class META:
        ordering = ['codigo']
        verbose_name_plural = "codigos"

class ciediez(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descriptor = models.CharField(max_length=255)
    capitulo_num = models.CharField(max_length=10, null=True, blank=True)
    capitulo_titulo = models.CharField(max_length=255, null=True, blank=True)
    grupo = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)
    OMSciediez = models.ForeignKey('oms2008ciediez', verbose_name='CIE 10-2008', null=True, blank=True)
    def __unicode__(self):
        return "%s | %s" % (self.codigo, self.descriptor)
    class Meta:
        ordering=['codigo']
        verbose_name_plural = "Codigos CIE-DEIS"

class ges_patologia(models.Model):
    id = models.IntegerField(primary_key=True)
    glosa = models.CharField(max_length=255)
    glosa_abrev = models.CharField(max_length=255, blank=True, help_text='Glosa Abreviada', verbose_name='Glosa Abreviada')
    ciediez = models.ManyToManyField('modeladorges.ciediez', blank=True, related_name="diagnostico")
    casproc = models.ManyToManyField('modeladorges.casprocedimiento', blank=True)
    casdiag = models.ManyToManyField('modeladorges.casdiagnostico', blank=True)
    def get_cie(objeto):
        return "<br/>".join([s.descriptor for s in objeto.ciediez.order_by('codigo').all()[:6]])
    get_cie.allow_tags = True
    get_cie.short_description = 'CIE-DEIS'
    def __unicode__(self):
        return self.glosa
    class Meta:
        ordering = ['id']

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
        return "%s | %s" % (self.idintervencionclinica, self.integlosa)
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
        return "%s | %s" % (self.codigo, self.descripcion)
    class Meta:
        ordering = ['codigo']




class concepto(models.Model):
    conceptid = models.BigIntegerField(primary_key=True)
    fsn = models.CharField('Fully Specified Name',max_length=255, )
    ciedeis = models.ForeignKey(ciediez, null=True, blank=True)
    cieDiez = models.ForeignKey(oms2008ciediez, null=True, blank=True)
    revisado = models.BooleanField()

    def __unicode__(self):
        return self.fsn

class descripcione(models.Model):
    descriptionid = models.BigIntegerField(primary_key=True)
    ocisid =  models.BigIntegerField(unique=True, )
    OPCIONES_TIPO = (
        (1,'Preferido'),
        (2,'Sinonimo Visible'),
        #        (3,'Sinonimo No Visible'),
        #        (4,'Termino No Valido'),
        )
    termino = models.CharField(max_length=255)
    id_concepto = models.ForeignKey(concepto, null=True, blank=True)
    tipodescripcion = models.IntegerField(choices=OPCIONES_TIPO)
    def __unicode__(self):
        return self.termino
    class Meta:
        ordering = ['descriptionid']
        verbose_name = "Descripciones"
