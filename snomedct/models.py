from django.db import models

# Create your models here.

class sct_concept(models.Model):
    OPCIONES_CONCEPTSTATUS = (
        (0,'Activo'),
        (1,'Retirado'),
        (2,'Duplicado'),
        (3,'Desactualizado'),
        (4,'Ambiguo'),
        (5,'Erroneo'),
        (6,'Limitado'),
        (10,'Trasladado a otra parte'),
        (11,'Traslado pendiente')
    )
    conceptid = models.BigIntegerField(primary_key=True)
    conceptstatus =  models.PositiveSmallIntegerField(choices=OPCIONES_CONCEPTSTATUS)
    fullyspecifiedname = models.CharField(max_length=255)
    ctv3id = models.CharField(max_length=20)
    snomedid = models.CharField(max_length=20)
    isprimitive = models.BooleanField()
    #sct_relationship = models.ManyToManyField('self', through=sct_relationship, symmetrical=False)
    def __unicode__(self):
        return u'%s - %s' %(self.conceptid,self.fullyspecifiedname)


class sct_relationship(models.Model):
    OPCIONES_CHARACTERISTICTYPE = (
        (0,'Definitorio'),
        (1,'Calificador'),
        (2,'Historico'),
        (3,'Adicional'),
        )
    OPCIONES_REFINABILITY = (
        (0,'No refinable'),
        (1,'Opcional'),
        (2,'Obligatorio'),
        )
    relationshipid = models.BigIntegerField(primary_key=True)
    conceptid1 = models.ForeignKey(sct_concept, related_name='padre')
#    relationshiptype = models.BigIntegerField()
    relationshiptype = models.ForeignKey(sct_concept, related_name='relacion')
    conceptid2 = models.ForeignKey(sct_concept, related_name='hijo')
    characteristictype = models.PositiveSmallIntegerField(choices=OPCIONES_CHARACTERISTICTYPE)
    refinability = models.PositiveSmallIntegerField(choices=OPCIONES_REFINABILITY)
    relationshipgroup = models.PositiveSmallIntegerField()
    def __unicode__(self):
        return u"%s | %s | %s" % (self.conceptid1,self.relationshiptype,self.conceptid2)

class sct_description(models.Model):
    OPCIONES_DESCRIPTIONSTATUS = (
    (0, 'Activo'),
    (1, 'No activo'),
    (2, 'Duplicado'),
    (3, 'Desactualizado'),
    (5, 'Erroneo'),
    (6, 'Limitado'),
    (7, 'Inapropiado'),
    (8, 'Concepto no activo'),
    (10, 'Trasladado a otra parte'),
    (11, 'Traslado pendiente'),
    )
    OPCIONES_INITIALCAPITALSTATUS = (
        (0,'Falso'),
        (1,'Verdadero')
    )
    OPCIONES_DESCRIPTIONTYPE = (
        (0, 'No especificado'),
        (1, 'Preferido'),
        (2, 'Sinonimo'),
        (3, 'FullySpecifiedName'),
    )
    descriptionid	= models.BigIntegerField(primary_key=True)
    descriptionstatus = models.PositiveSmallIntegerField(choices=OPCIONES_DESCRIPTIONSTATUS)
    conceptid	= models.ForeignKey(sct_concept)
    term	= models.CharField(max_length=255)
    initialcapitalstatus = models.PositiveSmallIntegerField(choices=OPCIONES_INITIALCAPITALSTATUS)
    descriptiontype	= models.PositiveSmallIntegerField(choices=OPCIONES_DESCRIPTIONTYPE)
    languagecode = models.CharField(max_length=20)
    def __unicode__(self):
        return self.term