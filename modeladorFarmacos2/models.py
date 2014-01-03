from django.core.urlresolvers import reverse
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
OPCIONES_BOOL = ((1,'Si'),(0,'No'))

# Create your models here.
class dbnet (models.Model):
    cod_clasificacion = models.IntegerField()
    clasificacion = models.CharField(max_length=255)
    codigo = models.IntegerField()
    producto = models.CharField(max_length=255)
    receta_retenida = models.IntegerField()
    cod_principio_activo = models.CharField(max_length=255)
    principio_activo = models.CharField(max_length=255)
    cod_concentracion = models.CharField(max_length=255)
    concentracion = models.CharField(max_length=255)
    cod_acc_farmacologica = models.IntegerField()
    accion_farmacologica = models.CharField(max_length=255)
    cod_unidad = models.CharField(max_length=255)
    unidad_medida = models.CharField(max_length=255)
    def __unicode__(self):
        return self.producto


class atc (models.Model):
    cod_atc = models.CharField(max_length=10, primary_key=True)
    n1_cod = models.CharField(max_length=10)
    n1_desc = models.CharField(max_length=255)
    n2_cod = models.CharField(max_length=10)
    n2_desc = models.CharField(max_length=255)
    n3_cod = models.CharField(max_length=10)
    n3_desc = models.CharField(max_length=255)
    n4_cod = models.CharField(max_length=10)
    n4_desc = models.CharField(max_length=255)
    nivelmax = models.IntegerField()
    largo = models.IntegerField()
    atc_desc = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s > %s > %s > %s > %s > %s" % (
             self.cod_atc
            ,self.atc_desc
            ,self.n1_desc
            ,self.n2_desc
            ,self.n3_desc
            ,self.n4_desc
            )
    class META:
        verbose_name_plural ='Codigos ATC'


## ##-
## table 'kairos_sustancia'
## tabla de sustancias de kairos
## ##-



class kairos_sustancia (models.Model):
    clave = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fechaalta = models.DateTimeField(null=True)
    fechacambio = models.DateTimeField(null=True)
    estado = models.CharField(max_length=1)

    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['clave']
        verbose_name_plural ='tabla de sustancias de kairos'

## ##-
## table 'kairos_lab'
## laboratorios de kairos
## ##-



class kairos_lab (models.Model):
    clave = models.IntegerField(primary_key=True)
    abreviatura = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    direccioni = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    codigopostal = models.CharField(max_length=255)
    telefonos = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    web = models.CharField(max_length=255)
    fechaalta = models.DateTimeField(null=True)
    fechacambio = models.DateTimeField(null=True)
    estado = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.abreviatura)
    class Meta:
        ordering=['clave']
        verbose_name_plural ='laboratorios de kairos'


## ##-
## table 'kairos_productos'
## tabla de productos de kairos
## ##-



class kairos_productos (models.Model):
    clave = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    laboratorioproductor = models.ForeignKey(kairos_lab, null=True,blank=True, related_name='productor')
    laboratoriocomercializador = models.ForeignKey(kairos_lab, null=True,blank=True, related_name='comercializador')
    origen = models.CharField(max_length=255)
    psicofarmaco = models.CharField(max_length=255)
    condicionventa = models.CharField(max_length=255)
    estupefaciente = models.CharField(max_length=255)
    almacenamiento = models.CharField(max_length=255)
    caducidad = models.CharField(max_length=255)
    certificado = models.CharField(max_length=255)
    fechaalta = models.DateTimeField(null=True)
    fechacambio = models.DateTimeField(null=True)
    estado = models.CharField(max_length=255)
    impuesto = models.CharField(max_length=255)
    odontologia = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s (%s) - %s" % (self.descripcion,self.laboratoriocomercializador,self.estado)
    class Meta:
        ordering=['clave']
        verbose_name_plural ='tabla de productos de kairos'

## ##-
## table 'kairos_presentaciones'
## tabla de presentaciones de productos de kairos
## ##-



class kairos_presentaciones (models.Model):
    id_presentacion_kairos = models.IntegerField(primary_key=True)
    claveproducto = models.ForeignKey(kairos_productos)
    clavepresentacion = models.SmallIntegerField()
    concentracion = models.SmallIntegerField()
    unidadconcentracion = models.CharField(max_length=255)
    especificacion = models.CharField(max_length=255)
    viaadministracion = models.CharField(max_length=255)
    medio = models.CharField(max_length=255)
    cantidadenvase = models.SmallIntegerField()
    dosis = models.SmallIntegerField()
    cantidadunidad = models.FloatField(null=True)
    unidadcantidad = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    factorfraccion = models.SmallIntegerField()
    impuesto = models.CharField(max_length=255)
    porcentajeimpuesto = models.SmallIntegerField()
    listadodescuento = models.CharField(max_length=255)
    uso = models.CharField(max_length=255)
    pami = models.CharField(max_length=255)
    troquel = models.SmallIntegerField()
    ioma = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    sifar = models.CharField(max_length=255)
    codigobarras = models.CharField(max_length=255)
    canasta = models.CharField(max_length=255)
    registro = models.CharField(max_length=255)
    fechaalta = models.DateTimeField(null=True)
    fechacambio = models.DateTimeField(null=True)
    estado = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s - %s" % (self.claveproducto,self.descripcion)
    class Meta:
        ordering=['id_presentacion_kairos']
        verbose_name_plural ='tabla de presentaciones de productos de kairos'



class kairos_precio(models.Model):
    id_presentacion_kairos = models.AutoField(primary_key=True)
    claveproducto = models.ForeignKey(kairos_productos)
    clavepresentacion = models.ForeignKey(kairos_presentaciones)
    fechaingreso = models.DateField(null=True)
    fechavigencia = models.DateField(null=True)
    preciofabrica = models.FloatField()
    preciopublico = models.FloatField()
    preciofabrica12 = models.FloatField()
    preciopublico12 = models.FloatField()
    preciofabrica17 = models.FloatField()
    preciopublico17 = models.FloatField()
    preciofabrica18 = models.FloatField()
    preciopublico18 = models.FloatField()
    preciofabrica19 = models.FloatField()
    preciopublico19 = models.FloatField()
    def __unicode__(self):
        return u"%s" % self.claveproducto


#########################################################################

## ##-
## table 'xt_unidad'
## unidad de dosis de extension
## ##-

#
#
#class xt_unidad (models.Model):
#    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
#
#    id_xt_unidad = models.AutoField(primary_key=True)
#
#    descripcion = models.CharField(max_length=255)
#
#    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
#    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
#    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
#    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')
#
#    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
#
##    '''
##    Terminos que salen desde ITServer
##    '''
#    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
#    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino')
#
#    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
#    hiba_term = models.CharField(max_length=255, null=True, blank=True)
#
#    observacion = models.CharField(max_length=255, blank=True, null=True)
#    cl_concepto = models.CharField(max_length=20, blank=True, null=True)
#
#    def __unicode__(self):
#        return self.descripcion
#    class Meta:
#        ordering=['id_xt_unidad']
#        verbose_name_plural ='XT unidad de dosis'

class xt_unidad_dosis_unitaria (models.Model):

    id_xt_unidad_dosis_u = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True,default=0)

    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_unidad_dosis_u']
        verbose_name_plural ='XT unidad de dosis unitaria'


class xt_unidad_medida_unitaria (models.Model):


    id_xt_unidad_medida_u = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True, default=0)

    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_unidad_medida_u']
        verbose_name_plural ='XT unidades de medida unitaria'


class xt_unidad_medida_cant (models.Model):
    id_unidad_medida_cant = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True, default=0)

    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['descripcion']
        verbose_name_plural ='XT unidad de medida de cantidad'



class xt_unidad_potencia (models.Model):
    id_unidad_potencia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True, default=0)

    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion

#########################################################################



class xt_forma_agrupada(models.Model):
    id_xt_forma_agrupada = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_ffa')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_ffa')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True, default=0)
#    '''
#    Terminos que salen desde ITServer
#    '''
    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['descripcion']
        verbose_name_plural ='XT Agrupador de formas farmaceuticas de extension'

## ##-
## table 'xt_formas_farm'
## formas farmaceuticas de extension
## ##-



class xt_forma_farm (models.Model):

    id_xt_formafarm = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_ffe')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_ffe')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True, default=0)
    forma_agrupada = models.ForeignKey(xt_forma_agrupada, null=True, blank=True)

#    '''
#    Terminos que salen desde ITServer
#    '''
    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_formafarm']
        verbose_name_plural ='XT formas farmaceuticas de extension'




## ##-
## table 'xt_condicion_venta'
## condiciones de venta de la extension
## ##-



class xt_condicion_venta (models.Model):

    id_xt_condventa = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_crea", null=False, blank=False, editable=False)
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_mod", null=True, blank=True, editable=False)

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    observacion = models.CharField(max_length=255,blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_condventa']
        verbose_name_plural ='XT condiciones de venta de la extension'




## ##-
## table ''
## extension de sustancias
## ##-



class xt_sustancia (models.Model):
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
            (2,'Primera Letra Mayuscula'),
            (3,'Sensible')
        )
    id_xt_sust = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=1)

    riesgo_teratogenico = models.CharField(max_length=15, null=True, blank=True)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False,blank=False, default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False, blank=False, default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False, blank=False, default=0)

#    '''
#    Terminos que salen desde ITServer
#    '''
    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)
    def __unicode__(self):
        return u"%s | %s | %s" % (self.id_xt_sust, self.estado, self.descripcion)
    class Meta:
        ordering=['id_xt_sust']
        verbose_name_plural ='XT extension de sustancias'



## ##-
## table 'xt_mb'
## medicamento basico
## ##-


class xt_mb (models.Model):
    OPCIONES_CREC = (
        (0, 'Autogenerado'),
            (1, 'Manual')
        )
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
            (2,'Primera Letra Mayuscula'),
            (3,'Sensible')
        )
    xt_id_mb = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=False, null=False)

#    '''
#    Campo determina si la descripcion es autogenerada al grabaar
#    el formulario o si debe mantener como texto libre del campo DESCRIPCION
#    '''
    creac_nombre = models.SmallIntegerField(max_length=1, choices=OPCIONES_CREC, null=False, blank=False, default=0)
#    '''
#
#    '''
    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=1)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_mod')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True,default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True, default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True,default=0)

#    '''
#    Terminos que salen desde ITServer
#    '''
    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino', null=True, blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    rel_xt_sust = models.ManyToManyField(xt_sustancia, through='rel_xt_mb_xt_sust')
    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True,null=True)

    def get_sustancia(objeto):
        return "<br/>".join([s.descripcion for s in objeto.rel_xt_sust.order_by('id_xt_sust').all()[:6]])
    get_sustancia.allow_tags = True
    get_sustancia.short_description = 'XT Sustancias'

    def __unicode__(self):
        return u"%s | %s | %s" % (self.xt_id_mb, self.estado, self.descripcion)
    class Meta:
        ordering=['xt_id_mb']
        verbose_name_plural ='XT medicamento basico (extension)'


## ##-
## table 'xt_mc'
## 
## ##-



class xt_mc (models.Model):

    OPCIONES_FORMA_FARM = ((1, 'Discreta'),(2,'Continua'),(3,'No Aplica'))
    OPCIONES_PRESCRIPCION = (
        (1,'Valido como MC prescribible')
        ,(2,'Nunca valido para prescribir como MC')
        ,(3,'No recomendable prescribir como MC')
        )
    OPCIONES_CREC = (
        (0, 'Autogenerado'),
            (1, 'Manual')
        )
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
            (2,'Primera Letra Mayuscula'),
            (3,'Sensible')
        )
    id_xt_mc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False, help_text='Obligatorio')
#    '''
#    Campo determina si la descripcion es autogenerada al grabaar
#    el formulario o si debe mantener como texto libre del campo DESCRIPCION
#    '''
    creac_nombre = models.SmallIntegerField(max_length=1, choices=OPCIONES_CREC, null=False, blank=False, default=0)
#    '''
#
#    '''
    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=1)

    med_basico = models.ForeignKey(xt_mb, null=False, blank=False, limit_choices_to = {'estado':'0'})
    estado_prescripcion = models.SmallIntegerField(choices=OPCIONES_PRESCRIPCION, null=False, blank=False, default=1)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)

    tipo_forma_farm = models.SmallIntegerField(choices=OPCIONES_FORMA_FARM, null=False, blank=False)

    u_logistica_cant = models.IntegerField("U_logistica_cant",null=True, blank=True)
    u_logistica_u = models.ForeignKey(xt_unidad_dosis_unitaria, null=True, blank=True, limit_choices_to = {'estado':'0'},related_name='u_logistica_u'
        ,verbose_name="U Logistica U")
    unidosis_asist_cant = models.FloatField("unidosis asist cant", blank=True,null=True)
    unidosis_asist_u = models.ForeignKey(xt_unidad_medida_unitaria, null=True, blank=True, limit_choices_to = {'estado':'0'}, related_name='unidosis_asist_u'
        , verbose_name="unidosis asist_u")
    volumen_total_cant = models.FloatField("Volumen Total num",null=True, blank=True)

    limit = models.Q(id_unidad_medida_cant = '25') | models.Q(id_unidad_medida_cant = '39') | models.Q(id_unidad_medida_cant = '40')
    volumen_total_u = models.ForeignKey(xt_unidad_medida_cant, null=True, blank=True
        , verbose_name='Volumen total U'
        , limit_choices_to = limit
        , related_name='volumen_total_u' )

    forma_farmaceutica_agrup = models.ForeignKey(xt_forma_agrupada, null=True, blank=True, limit_choices_to = {'estado':'0'})

    #condicion_venta debe ir como radiobutton de las 4 opciones de la otra table
    condicion_venta = models.ForeignKey(xt_condicion_venta, null=True, blank=True, limit_choices_to = {'estado':'0'})
#    '''
#    Terminos que salen desde ITServer
#    '''
    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino',blank=True, null=True)

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    atc_code = models.ForeignKey(atc, null=True, blank=True)


    medlineplus_ulr = models.URLField("URL a MedlinePlus",max_length=255, blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)

    cl_concepto = models.CharField(max_length=20, blank=True, null=True)

    rel_mc_sust = models.ManyToManyField(xt_sustancia, through='rel_mc_sust')

    def get_pc(self):
        return '<br/>'.join([k.descripcion for k in self.xt_pc_set.order_by('id_xt_pc').all()[:6]])
    get_pc.allow_tags = True
    get_pc.short_description = 'XT Producto Comercial'

    def get_sustancia(objeto):
        return "<br/>".join([s.descripcion for s in objeto.rel_mc_sust.order_by('id_xt_sust').all()[:6]])
    get_sustancia.allow_tags = True
    get_sustancia.short_description = 'XT Sustancias'

    def get_atc(object):
        return object.atc_code
    get_atc.short_description = 'ATC'

    def descrip_auto(self):
        return 'KAM%s' % self.med_basico


    def __unicode__(self):
        return u"%s | %s | %s" % (self.id_xt_mc, self.estado, self.descripcion)

    class Meta:
        ordering=['descripcion']
        verbose_name_plural = "XT medicamento clinico (extension)"


## ##-
## table 'rel_mc_sust'
##
## ##-


class rel_mc_sust (models.Model):
    id_rel_mc_sust = models.AutoField(primary_key=True)
    id_xt_mc = models.ForeignKey(xt_mc, related_name='relacion_xt_mc    ')

    id_xt_sust = models.ForeignKey(xt_sustancia)

    orden = models.SmallIntegerField(null=True, blank=True)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO)
    potencia = models.FloatField(null=True, blank=True)

    id_unidad_potencia = models.ForeignKey(xt_unidad_potencia, related_name='%(app_label)s_%(class)s_related_potencia', null=True, blank=True)
    partido_por = models.FloatField(null=True,blank=True)
    id_unidad_partido_por = models.ForeignKey(xt_unidad_potencia, related_name='%(app_label)s_%(class)s_related_partido',null=True, blank=True)



## ##-
## table 'rel_xt_mb_xt_sust'
##
## ##-



class rel_xt_mb_xt_sust (models.Model):
    id_rel_xt_mb_xt_sust = models.AutoField(primary_key=True)
    id_xt_sust = models.ForeignKey(xt_sustancia)
    id_xt_mb = models.ForeignKey(xt_mb)
    orden = models.SmallIntegerField(null=True, blank=False)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO)



## ##-
## table 'xt_laboratorio'
## laboratorios de la extension
## ##-


class xt_laboratorio (models.Model):
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
            (2,'Primera Letra Mayuscula'),
            (3,'Sensible')
        )
    id_xt_lab = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    desc_abrev = models.CharField(max_length=255, blank=False)

    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=3)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False, default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False, default=0)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u"%s | %s | %s" % (self.id_xt_lab, self.estado, self.desc_abrev)
    class Meta:
        ordering=['id_xt_lab']
        verbose_name_plural ='XT laboratorios de la extension'



## ##-
## table 'xt_gfp'
## grupo de familia de productos de la extension
## ##-



class xt_gfp (models.Model):
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
            (2,'Primera Letra Mayuscula'),
            (3,'Sensible')
        )
    id_xt_gfp = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=1)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False ,default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False ,default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False ,default=0)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_gfp']
        verbose_name_plural ='XT grupo de familia de productos de la extension'


## ##-
## table 'xt_fp'
## familia de producto de la extension
## ##-


class xt_fp (models.Model):
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
            (2,'Primera Letra Mayuscula'),
            (3,'Sensible')
        )
    id_xt_fp = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=1)

    familia_generica = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_BOOL, default=0, blank=False,null=False)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False,default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False,default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False,default=0)

    id_gfp_xt = models.ForeignKey(xt_gfp, null=True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_fp']
        verbose_name_plural ='XT familia de producto de la extension'


class xt_sabor (models.Model):
    id_xt_sabor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_sabor')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_sabor')

#    '''
#    Terminos que salen desde ITServer
#    '''
    sn_descriptionid = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'SNOMED-CT DescriptionID')
    sn_term =   models.CharField(max_length=255, verbose_name=u'SNOMED-CT Termino')

    hiba_descriptionid = models.CharField(max_length=20, null=True, blank=True)
    hiba_term = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.descripcion

## ##-
## table 'xt_pc'
## productos comerciales de la extension
## ##-

class xt_pc (models.Model):
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
        (2,'Primera Letra Mayuscula'),
        (3,'Sensible'),
        )
    OPCIONES_CREC = (
        (0, 'Autogenerado'),
        (1, 'Manual'),
        )
    id_xt_pc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    descripcion_abreviada = models.CharField(max_length=255, verbose_name='Descripcion Abreviada', blank=True)

    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1
        , choices=OPCIONES_SENSIBLE
        , blank=False, null=False
        , default=3)

    creac_nombre = models.SmallIntegerField(max_length=1, choices=OPCIONES_CREC, null=False, blank=False, default=0)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.SmallIntegerField(choices=OPCIONES_ESTADO, null=False, blank=False, default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False, blank=False, default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False, blank=False, default=0)
    comercial_cl = models.PositiveSmallIntegerField(
        max_length=1,
        choices=OPCIONES_BOOL,
        null  = False,
        blank = False,
        verbose_name= 'Comecializado en Chile',
        default='1'
    )
    forma_farm_extendida = models.ForeignKey(xt_forma_farm, null=True,blank=True)

    sabor = models.ForeignKey(xt_sabor, null=True,blank=True)

    id_xt_fp = models.ForeignKey(xt_fp, verbose_name='Familia de Producto', null=True, blank=True)
    id_xt_mc = models.ForeignKey(xt_mc, verbose_name='Medicamento Clinico', null=True, blank=True)

    id_xt_lab = models.ForeignKey(xt_laboratorio, verbose_name=u'Laboratorio', null=True, blank=False)

    hiba_descriptionid = models.CharField(max_length=20, null = True, blank=True)
    hiba_term = models.CharField(max_length=255, null = True, blank=True)


    reg_isp_num = models.CharField(max_length=10, null = True, blank=True)
    reg_isp_ano = models.PositiveIntegerField(max_length=4, null=True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)

    equivalente = models.ManyToManyField('self', through='xt_bioequivalente', symmetrical=False)

    def __unicode__(self):
        return u"%s | %s | %s" % (self.id_xt_pc, self.estado, self.descripcion)
    class Meta:
        ordering=['descripcion']
        verbose_name_plural ='XT productos comerciales (extension)'




## ##-
## table 'xt_mcce'
## medicamento clinico con envase (extension)
## ##-


class xt_mcce (models.Model):
    OPCIONES_TIPO = (
        (1,'UNIDOSIS'),
        (2,'ENVASE CLINICO'),
        (3,'VENTA PUBLICO'),
        (4,'MUESTRA MEDICA'),
        (5,'FRACCIONADO')
        )
    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
        (2,'Primera Letra Mayuscula'),
        (3,'Sensible'),
        )
    OPCIONES_CREC = (
        (0, 'Autogenerado'),
        (1, 'Manual'),
        )
    id_xt_mcce = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=1)

    creac_nombre = models.SmallIntegerField(max_length=1, choices=OPCIONES_CREC, null=False, blank=False, default=0)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default=0)

    tipo = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_TIPO, null=False, blank=False)

    id_xt_mc = models.ForeignKey(xt_mc, verbose_name='Medicamento Clinico')

    cantidad = models.IntegerField()
    unidad_medida_cant = models.ForeignKey(xt_unidad_medida_cant, related_name='un_medida_cant')

    pack_multi_cant = models.IntegerField(null=True, blank=True)
    pack_multi_u = models.ForeignKey(xt_unidad_medida_cant, related_name='pack_multi_unidad',null=True, blank=True)

    volumen_total_cant = models.FloatField(null = True, blank=True)
    limit = models.Q(id_unidad_medida_cant = '25') | models.Q(id_unidad_medida_cant = '39') | models.Q(id_unidad_medida_cant = '40')
    volumen_total_u = models.ForeignKey(xt_unidad_medida_cant, related_name='vol_total_u' , null=True, blank=True
        , limit_choices_to = limit
        , verbose_name='Volumen total U' )

    hiba_descriptionid = models.CharField(max_length=20, null = True, blank=True)
    hiba_term = models.CharField(max_length=255, null = True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        return u"%s | %s | %s (%s)" % (self.id_xt_mcce, self.estado, self.descripcion, self.tipo)
    class Meta:
        ordering=['id_xt_mcce']
        verbose_name_plural ='XT medicamento clinico con envase (extension)'


## ##-
## table 'xt_pcce'
## productos comerciales con envase de la extension
## ##-



class xt_pcce (models.Model):

    OPCIONES_SENSIBLE = (
        (1,'Insensible'),
        (2,'Primera Letra Mayuscula'),
        (3,'Sensible')
        )
    OPCIONES_CREC = (
        (0, 'Autogenerado'),
        (1, 'Manual')
        )
    OPCIONES_TIPO_GTIN = (
        (1,'HE'),
        (2,'UC'),
        (3,'IC')
        )
    id_xt_pcce = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    desc_abreviada = models.CharField(max_length=255,blank=True)

    sensible_mayusc = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_SENSIBLE, blank=False, null=False, default=3)

    creac_nombre = models.SmallIntegerField(max_length=1, choices=OPCIONES_CREC, null=False, blank=False, default=0)


    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='%(app_label)s_%(class)s_related_crea')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='%(app_label)s_%(class)s_related_modif')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False,default=0)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False,default=0)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=False,default=0)
    #'''
    #Campos relacionados con el catalogo de compras de CENABAST
    #'''
    pack_cant = models.IntegerField(max_length=6, null=True,blank=True)
    pack_u =    models.ForeignKey(xt_unidad_medida_cant, null=True,blank=True)

    id_xt_pc = models.ForeignKey(xt_pc, verbose_name= 'Producto Comercial', null=False)
    id_xt_mcce = models.ForeignKey(xt_mcce, verbose_name='Medicamento Clinico Con Envase', null=True,blank=True)

    gtin_gs1 = models.BigIntegerField(blank=True, null=True)
    existencia_gs1 = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL,null=True,blank=True, verbose_name=u'Existe en GS1')

    id_presentacion_kairos = models.ForeignKey(kairos_presentaciones, verbose_name='Presentacion Kairos',blank=True, null=True)
    existencia_kairos = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL,null=True,blank=True, verbose_name=u'Existe en Kairos')

    codigo_cenabast = models.IntegerField(max_length=20, blank=True,null=True)
    codigo_dbnet = models.ForeignKey(dbnet, null=True,blank=True)

    hiba_descriptionid = models.CharField(max_length=20, null = True, blank=True)
    hiba_term = models.CharField(max_length=255, null = True, blank=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    cl_concepto = models.CharField(max_length=20, null=True, blank=True)

    def fue_modif_reciente(self):
        return self.fecha_ult_mod >= timezone.now() - datetime.timedelta(days=1)
    fue_modif_reciente.admin_order_field = 'fecha_ult_mod'
    fue_modif_reciente.boolean = True
    fue_modif_reciente.short_description = 'Modificado Recientemente?'

    def __unicode__(self):
        return u"%s | %s | %s" % (self.id_xt_pcce, self.estado, self.descripcion)

    class Meta:
        ordering=['id_xt_pcce']
        verbose_name_plural ='XT productos comerciales con envase (extension)'

    def get_absolute_url(self):

        return reverse('pcce-detalle', kwargs={'pk': self.id_xt_pcce})



class xt_bioequivalente(models.Model):
    id_xt_bioequivalente = models.AutoField(primary_key=True)
    bioequivalente = models.ForeignKey(xt_pc, related_name='bequivalente')
    referencia = models.ForeignKey(xt_pc, related_name='referencial')

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='usuariocrea_bioeq')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_bioeq')

    def __unicode__(self):
        return u"%s | %s" % (self.referencia, self.bioequivalente)
    class Meta:
        ordering=['id_xt_bioequivalente']
        verbose_name_plural ='XT Productos Bioequivalentes'

