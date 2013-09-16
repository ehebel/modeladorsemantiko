from django.db import models


class concepto(models.Model):
    fsn = models.CharField('Fully Specified Name',max_length=255, )
    revisado = models.BooleanField()
    def descripciones(objeto):
        return '<br/>'.join(c.termino for c in objeto.descripcion_set.order_by('id')[:3])
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
    ExamCode = models.CharField(max_length=255, primary_key=True)
    ExamName = models.CharField(max_length=255)
    codigoporarea = models.ManyToManyField(conceptosCASporarea)
    def get_conceptosporarea(objeto):
        return "<br/>".join([s.concepto for s in objeto.get_conceptosporarea.order_by('id').all[:6]])
    get_conceptosporarea.allow_tags = True
    get_conceptosporarea.short_description = 'Conceptos por Area'
    def __unicode__(self):
        return self.ExamName
    class Meta:
        ordering=['ExamName']
        verbose_name_plural = "efectores"

