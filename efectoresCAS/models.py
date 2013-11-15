from django.db import models


class concepto(models.Model):
    OPCIONES_DOMINIO = ((1, 'Imagenes'),(2, 'Procedimientos'),(3,'Laboratorio'),(4,'Takion'))
    fsn = models.CharField('Fully Specified Name',max_length=255, )
    revisado = models.BooleanField()
    dominio = models.IntegerField(choices=OPCIONES_DOMINIO)
    pedible = models.BooleanField()
    def descripciones(objeto):
        return '<br/>'.join(c.termino for c in objeto.descripcion_set.order_by('id')[:4])

    descripciones.allow_tags = True
    descripciones.short_description = 'Descripcion'
    def __unicode__(self):
        return self.fsn
    class Meta:
        ordering=['id']
        verbose_name_plural = "conceptos"

class cas_area(models.Model):
    descripcion = models.CharField(max_length=255)
    conceptosporarea = models.ManyToManyField(concepto, through='conceptosCASporarea')
    def conceptos (objeto):
        return '<br/>'.join(c.fsn for c in objeto.conceptosporarea.order_by('id')[:4])
    conceptos.allow_tags = True
    conceptos.short_description = 'Conceptos'
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id']
        verbose_name_plural = "Areas CAS"

class cas_lugar(models.Model):
    descripcion = models.CharField(max_length=255)
    areas = models.ForeignKey(cas_area)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id']
        verbose_name_plural = "Lugares CAS"

class conceptosCASporarea(models.Model):
    concepto = models.ForeignKey(concepto)
    area = models.ForeignKey(cas_area)
    def get_efectorxarea(objeto):
        pass
    get_efectorxarea.allow_tags = True
    get_efectorxarea.short_description = 'Efectores por Concepto-Area (En desarrollo)'
    def __unicode__(self):
        return "%s | %s" % (self.concepto.fsn, self.area.descripcion)
    class Meta:
        ordering=['id']
        verbose_name_plural = "Conceptos CAS por Area"


class descripcion(models.Model):
    OPCIONES_TIPO = (
        (1,'Preferido'),
        (2,'Sinonimo Visible'),
        #        (3,'Descripcion Completa'),
        #        (4,'Error tipografico'),
        )
    termino = models.CharField(max_length=255)
    id_concepto = models.ForeignKey(concepto, null=True, blank=True)
    tipodescripcion = models.IntegerField(choices=OPCIONES_TIPO)
    def __unicode__(self):
        return self.termino
    class Meta:
        ordering=['id']
        verbose_name_plural = "descripciones"



class efector(models.Model):
    OPCIONES_DOMINIO = ((1, 'Imagenes'),(2, 'Procedimientos'),(3,'Laboratorio'))
    ExamCode = models.CharField(max_length=255, primary_key=True)
    ExamName = models.CharField(max_length=255)
    dominio = models.IntegerField(choices=OPCIONES_DOMINIO)
    codigoporarea = models.ManyToManyField(conceptosCASporarea, through='efector_codigoporarea')
    def get_conceptosporarea(objeto):
        return '<br/>'.join(c.concepto.fsn for c in objeto.codigoporarea.order_by('id')[:4])
    get_conceptosporarea.allow_tags = True
    get_conceptosporarea.short_description = 'Conceptos'
    def get_areas(objeto):
        return '<br/>'.join(c.area.descripcion for c in objeto.codigoporarea.order_by('id')[:4])
    get_areas.allow_tags = True
    get_areas.short_description = 'Areas'
    def __unicode__(self):
        return '%s | %s' % (self.ExamCode,self.ExamName)
    class Meta:
        ordering=['ExamName']
        verbose_name_plural = "efectores"


class efector_codigoporarea(models.Model):
    efector = models.ForeignKey(efector)
    conceptoscasporarea = models.ForeignKey(conceptosCASporarea)
    def __unicode__(self):
        return u'%s' % self.id