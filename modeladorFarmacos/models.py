from django.db import models
from django.contrib.auth.models import User
#from django.db.models import Q

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
        return u"%s > %s > %s > %s > %s > %s" % (self.cod_atc,self.atc_desc,self.n1_desc,self.n2_desc,self.n3_desc,self.n4_desc)
    class META:
        verbose_name_plural ='Codigos ATC'


class vtm_hiba (models.Model):
    descriptionid = models.BigIntegerField(primary_key=True)
    term_vtm = models.CharField(max_length=255)
    def __unicode__(self):
        return self.term_vtm


class vmp_hiba (models.Model):
    descriptionid = models.BigIntegerField(primary_key=True)
    term_vmp = models.CharField(max_length=255)
    def __unicode__(self):
        return self.term_vmp


## ##-
## table 'uk_dmd_conceptos'
##
## ##-


class uk_dmd_conceptos (models.Model):
    conceptid = models.BigIntegerField(primary_key=True)
    conceptstatus = models.SmallIntegerField()
    fullyspecifiedname = models.CharField(max_length=255)
    ctv3id = models.CharField(max_length=255)
    snomedid = models.CharField(max_length=255)
    isprimitive = models.SmallIntegerField()
    relationship = models.ManyToManyField('self', through='uk_dmd_relationships', symmetrical=False)
    #, limit_choices_to = {'area':'P'})
    def __unicode__(self):
        return self.fullyspecifiedname

## ##-
## table 'uk_dmd_relationships'
## tabla de relaciones de dm+d
## ##-


#TODO Definir relacion recursiva TABLA DM+D
class uk_dmd_relationships (models.Model):
    relationshipid = models.BigIntegerField(primary_key=True)
    conceptid1 = models.ForeignKey(uk_dmd_conceptos, related_name='Concepto 1')
    #TODO OJO: este campo no esta vinculado.
    relationshiptype = models.BigIntegerField()
    conceptid2 = models.ForeignKey(uk_dmd_conceptos, related_name='Concepto 2')
    characteristictype = models.SmallIntegerField()
    refinability = models.SmallIntegerField()
    relationshipgroup = models.SmallIntegerField()


    class Meta:
        ordering=['relationshipid']
        verbose_name_plural ='tabla de relaciones de dm+d'

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
        return u'%s [%s]' % (self.abreviatura,self.descripcion)
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



## ##-
## table 'xt_unidad_dosis_unitaria'
## unidad de dosis unitaria de extension
## ##-



class xt_unidad_dosis_unitaria (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))

    id_xt_unidad_dosis_u = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_udu')
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_unidad_dosis_u']
        verbose_name_plural ='XT unidad de dosis unitaria'


## ##-
## table 'xt_unidad_medida_unitaria'
## unidades de medida unitaria para la extension
## ##-



class xt_unidad_medida_unitaria (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))

    id_xt_unidad_medida_u = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_umu')
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_unidad_medida_u']
        verbose_name_plural ='XT unidades de medida unitaria'



class xt_formas_agrupadas(models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    id_xt_formas_agrupadas = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_fa')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['descripcion']
        verbose_name_plural ='XT Agrupador de formas farmaceuticas de extension'

## ##-
## table 'xt_formas_farm'
## formas farmaceuticas de extension
## ##-



class xt_formas_farm (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))

    id_xt_formafarm = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_ff')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    id_formas_agrupadas = models.ForeignKey(xt_formas_agrupadas, null=True, blank=True)
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
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))

    id_xt_condventa = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_cv')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)

    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_condventa']
        verbose_name_plural ='XT condiciones de venta de la extension'




## ##-
## table 'xt_sustancias'
## extension de sustancias
## ##-



class xt_sustancias (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_sust = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    riesgo_teratogenico = models.CharField(max_length=15, null=True, blank=True)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_sust')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_sust')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)

    concept_sust_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
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
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    xt_id_mb = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_mb')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_mb')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)

    kairos_sustancia = models.ForeignKey(kairos_sustancia,null=True,blank=True)
    concept_vtm_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    concept_vtm_hiba = models.ForeignKey(vtm_hiba, null = True, blank=True)


    rel_xt_sust = models.ManyToManyField(xt_sustancias, through='rel_xt_mb_xt_sust')
    observacion = models.CharField(max_length=255, blank=True, null=True)
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
## table 'xt_unidad_medida_cant'
## unidad de medida de cantidad de la extension
## ##-



class xt_unidad_medida_cant (models.Model):
    id_unidad_medida_cant = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['descripcion']
        verbose_name_plural ='XT unidad de medida de cantidad'


class xt_mc (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))

    OPCIONES_FORMA_FARM = ((1, 'Discreta'),(2,'Continua'),(3,'No Aplica'))
    OPCIONES_PRESCRIPCION = (
         (1,'Invalido para prescribir en Atencion Primaria')
        ,(2,'Nunca valido para prescribir como MC')
        #,(3,'No prescribible como un MC pero es valido como PC')
        #,(4,'No recomendable prescribir como un MC')
        ,(5,'Valido como producto prescribible')
        ,(6,'MC no recomendable para prescribir - marca no bioequivalente')
        ,(7,'MC no recomendable para prescribir - requiere entrenamiento del paciente')
        )
    id_xt_mc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False, help_text='Obligatorio')
    med_basico = models.ForeignKey(xt_mb, null=True, blank=True, limit_choices_to = {'estado':'0'})
    estado_prescripcion = models.SmallIntegerField(choices=OPCIONES_PRESCRIPCION, null=True, blank=True)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_mc')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='usuariomod_mc')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)

    tipo_forma_farm = models.SmallIntegerField(choices=OPCIONES_FORMA_FARM, null=True, blank=True)

    u_logistica_cant = models.IntegerField("U_logistica_cant",null=True, blank=True)
    u_logistica_u = models.ForeignKey(xt_unidad_dosis_unitaria, null=True, blank=True, limit_choices_to = {'estado':'0'}, verbose_name="U Logistica U")
    unidosis_asist_cant = models.FloatField("unidosis asist cant", blank=True,null=True)
    unidosis_asist_u = models.ForeignKey(xt_unidad_medida_unitaria, null=True, blank=True, limit_choices_to = {'estado':'0'}, verbose_name="unidosis asist_u")
    volumen_total_cant = models.FloatField("Volumen Total num",null=True, blank=True)

    limit = models.Q(id_unidad_medida_cant = '25') | models.Q(id_unidad_medida_cant = '39') | models.Q(id_unidad_medida_cant = '40')
    volumen_total_u = models.ForeignKey(xt_unidad_medida_cant, null=True, blank=True
        , verbose_name='Volumen total U'
        , limit_choices_to = limit)
    forma_farmaceutica_agrup = models.ForeignKey(xt_formas_agrupadas, null=True, blank=True, limit_choices_to = {'estado':'0'})
    condicion_venta = models.ForeignKey(xt_condicion_venta, null=True, blank=True, limit_choices_to = {'estado':'0'})
    concept_vmp_dmd = models.ForeignKey(uk_dmd_conceptos, null=True, blank=True)
    concept_vmp_hiba = models.ForeignKey(vmp_hiba, null=True, blank=True)
    atc_code = models.ForeignKey(atc, null=True, blank=True)

    rel_mc = models.ManyToManyField(xt_sustancias, through='rel_mc_sust')
    observacion = models.CharField(max_length=255, blank=True, null=True)
    medlineplus_ulr = models.URLField("URL a MedlinePlus",max_length=255, blank=True, null=True)
    descrip_auto = models.CharField(blank=True, default='')

    def get_pc(self):
        return '<br/>'.join([k.descripcion for k in self.xt_pc_set.order_by('id_xt_pc').all()[:6]])
    get_pc.allow_tags = True
    get_pc.short_description = 'XT Producto Comercial'

    def get_sustancia(objeto):
        return "<br/>".join([s.descripcion for s in objeto.rel_mc.order_by('id_xt_sust').all()[:6]])
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
## table 'xt_unidad_potencia'
##
## ##-

class xt_unidad_potencia (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    id_unidad_potencia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion


## ##-
## table 'rel_mc_sust'
##
## ##-


class rel_mc_sust (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    id_rel_mc_sust = models.AutoField(primary_key=True)
    id_xt_mc = models.ForeignKey(xt_mc)
    id_xt_sust = models.ForeignKey(xt_sustancias)
    orden = models.SmallIntegerField(null=True, blank=True)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO)
    potencia = models.FloatField(null=True, blank=True)
    id_unidad_potencia = models.ForeignKey(xt_unidad_potencia, related_name='unidad potencia', null=True, blank=True)
    partido_por = models.FloatField(null=True,blank=True)
    id_unidad_partido_por = models.ForeignKey(xt_unidad_potencia, related_name='unidad partido por',null=True, blank=True)



## ##-
## table 'rel_xt_mb_xt_sust'
##
## ##-



class rel_xt_mb_xt_sust (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    id_rel_xt_mb_xt_sust = models.AutoField(primary_key=True)
    id_xt_sust = models.ForeignKey(xt_sustancias)
    id_xt_mb = models.ForeignKey(xt_mb)
    orden = models.SmallIntegerField(null=True, blank=False)
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO)



## ##-
## table 'xt_laboratorio'
## laboratorios de la extension
## ##-


class xt_laboratorio (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_lab = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    desc_abrev = models.CharField(max_length=255, blank=True)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_lab')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='usuariomod_lab')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    clave_lab_kairos = models.ForeignKey(kairos_lab, null=True, blank=True)

    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_lab']
        verbose_name_plural ='XT laboratorios de la extension'


## ##-
## table 'xt_producto'
## productos de la extension
## ##-



class xt_producto (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    estado = models.SmallIntegerField(choices=OPCIONES_ESTADO, null=False, blank=False)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_producto')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_producto')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')

    id_xt_lab = models.ForeignKey(xt_laboratorio, null=True , blank=True, limit_choices_to = {'estado':'0'})
    clave_prod_kairos = models.ForeignKey(kairos_productos,blank=True,null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_producto']
        verbose_name_plural ='XT productos de la extension'


## ##-
## table 'xt_gfp'
## grupo de familia de productos de la extension
## ##-



class xt_gfp (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_gfp = models.AutoField(primary_key=True)

    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_gfp')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='usuariomod_gfp')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)

    concept_tfg_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
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
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_fp = models.AutoField(primary_key=True)
    xtconcepto = models.SmallIntegerField()
    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=True, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_fp')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='usuariomod_fp')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, null=True)

    id_producto_xt = models.ForeignKey(xt_producto, null=True, limit_choices_to = {'estado':'0'})
    id_gfp_xt = models.ForeignKey(xt_gfp, null=True, blank=True)
    concept_tf_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_fp']
        verbose_name_plural ='XT familia de producto de la extension'




## ##-
## table 'xt_pc'
## productos comerciales de la extension
## ##-

class xt_pc (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_pc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    descripcion_breviada = models.CharField(max_length=255, verbose_name='Descripcion Abreviada', blank=True)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_pc')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_pc')

    estado = models.SmallIntegerField(choices=OPCIONES_ESTADO, null=False, blank=False)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')

    id_xt_fp = models.ForeignKey(xt_fp, verbose_name='Familia de Producto', null=True, blank=True)
    id_xt_mc = models.ForeignKey(xt_mc, verbose_name='Medicamento Clinico', null=True, blank=True)
    concept_amp_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    reg_isp_num = models.CharField(max_length=10, null = True, blank=True)
    reg_isp_ano = models.PositiveIntegerField(max_length=2, null=True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
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
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    OPCIONES_TIPO = (
        (1,'UNIDOSIS'),
        (2,'ENVASE CLINICO'),
        (3,'VENTA PUBLICO'),
        (4,'MUESTRA MEDICA'),
        (5,'FRACCIONADO')
    )
    id_xt_mcce = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_mcce')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=False, editable=False, related_name='usuariomod_mcce')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default='Unspecified')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    tipo = models.PositiveSmallIntegerField(max_length=1, choices=OPCIONES_TIPO, null=False, blank=False)

    id_xt_mc = models.ForeignKey(xt_mc, verbose_name='Medicamento Clinico')
    cantidad = models.IntegerField()
    unidad_medida_cant = models.ForeignKey(xt_unidad_medida_cant, related_name='un_medida_cant')
    concept_vmpp_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)

    volumen_total_cant = models.FloatField(null = True, blank=True)

    limit = models.Q(id_unidad_medida_cant = '25') | models.Q(id_unidad_medida_cant = '39') | models.Q(id_unidad_medida_cant = '40')

    volumen_total_u = models.ForeignKey(xt_unidad_medida_cant, related_name='vol_total_u' , null=True, blank=True
        , limit_choices_to = limit
        , verbose_name='Volumen total U' )
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return u"%s | %s | %s" % (self.id_xt_mcce, self.estado, self.descripcion)
    class Meta:
        ordering=['id_xt_mcce']
        verbose_name_plural ='XT medicamento clinico con envase (extension)'


## ##-
## table 'xt_pcce'
## productos comerciales con envase de la extension
## ##-



class xt_pcce (models.Model):
    OPCIONES_ESTADO = ((0, 'Vigente'),(1, 'No Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_pcce = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    desc_abreviada = models.CharField(max_length=255,blank=True)

    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_pcce')
    fecha_ult_mod = models.DateTimeField(null=True, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_pcce')

    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default='Unspecified')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')

    id_xt_pc = models.ForeignKey(xt_pc, verbose_name= 'Producto Comercial')
    id_xt_mcce = models.ForeignKey(xt_mcce, verbose_name='Medicamento Clinico Con Envase')
    concept_dbnet = models.ForeignKey(dbnet, null=True, blank=True)
    gtin_gs1 = models.BigIntegerField(blank=True, null=True)
    concept_ampp_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    id_presentacion_kairos = models.ForeignKey(kairos_presentaciones, verbose_name='Presentacion Kairos',blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return u"%s | %s | %s" % (self.id_xt_pcce, self.estado, self.descripcion)
    class Meta:
        ordering=['id_xt_pcce']
        verbose_name_plural ='XT productos comerciales con envase (extension)'




class xt_bioequivalente(models.Model):
    id_xt_bioequivalente = models.AutoField(primary_key=True)
    bioequivalente = models.ForeignKey(xt_pc, related_name='bequivalente')
    referencia = models.ForeignKey(xt_pc, related_name='referencial')
    def __unicode__(self):
        return u"%s | %s" % (self.referencia, self.bioequivalente)
    class Meta:
        ordering=['id_xt_bioequivalente']
        verbose_name_plural ='XT Productos Bioequivalentes'