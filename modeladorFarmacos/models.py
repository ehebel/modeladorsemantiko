from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
## table 'xt_unidad_dosis_unitaria'
## unidad de dosis unitaria de extension
## ##-



class xt_unidad_dosis_unitaria (models.Model):
    id_xt_unidad_dosis_u = models.IntegerField(primary_key=True)
    
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    estado = models.BooleanField()
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_unidad_dosis_u']
        verbose_name_plural ='unidad de dosis unitaria de extension'


## ##-
## table 'xt_unidad_medida_unitaria'
## unidades de medida unitaria para la extension
## ##-



class xt_unidad_medida_unitaria (models.Model):
    id_xt_unidad_medida_u = models.SmallIntegerField()
    
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    estado = models.BooleanField()
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_unidad_medida_u']
        verbose_name_plural ='unidades de medida unitaria para la extension'


## ##-
## table 'xt_formas_farm'
## formas farmaceuticas de extension
## ##-



class xt_formas_farm (models.Model):
    id_xt_formafarm = models.IntegerField(primary_key=True)
    
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    estado = models.BooleanField()
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_formafarm']
        verbose_name_plural ='formas farmaceuticas de extension'




## ##-
## table 'xt_condicion_venta'
## condiciones de venta de la extension
## ##-



class xt_condicion_venta (models.Model):
    id_xt_condventa = models.IntegerField(primary_key=True)
    
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    estado = models.BooleanField()
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_condventa']
        verbose_name_plural ='condiciones de venta de la extension'


## ##-
## table 'kairos_sustancia'
## tabla de sustancias de kairos
## ##-



class kairos_sustancia (models.Model):
    clave = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fechaalta = models.DateTimeField()
    fechacambio = models.DateTimeField()
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
    fechaalta = models.DateTimeField()
    fechacambio = models.DateTimeField()
    estado = models.CharField(max_length=255)

    def __unicode__(self):
        return self.descripcion
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
    laboratorioproductor = models.SmallIntegerField()
    laboratoriocomercializador = models.SmallIntegerField()
    origen = models.CharField(max_length=255)
    psicofarmaco = models.CharField(max_length=255)
    condicionventa = models.CharField(max_length=255)
    estupefaciente = models.CharField(max_length=255)
    almacenamiento = models.CharField(max_length=255)
    caducidad = models.CharField(max_length=255)
    certificado = models.CharField(max_length=255)
    fechaalta = models.DateTimeField()
    fechacambio = models.DateTimeField()
    estado = models.CharField(max_length=255)
    impuesto = models.CharField(max_length=255)
    odontologia = models.CharField(max_length=255)

    def __unicode__(self):
        return self.descripcion
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
    fechaalta = models.DateTimeField()
    fechacambio = models.DateTimeField()
    estado = models.CharField(max_length=255)

    def __unicode__(self):
        return self.especificacion
    class Meta:
        ordering=['id_presentacion_kairos']
        verbose_name_plural ='tabla de presentaciones de productos de kairos'



class kairos_precio(models.Model):
    id_presentacion_kairos = models.AutoField(primary_key=True)
    claveproducto = models.IntegerField()
    clavepresentacion = models.IntegerField()
    fechaingreso = models.DateField()
    fechavigencia = models.DateField()
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
        return self.especificacion



## ##-
## table 'xt_sustancias'
## extension de sustancias
## ##-



class xt_sustancias (models.Model):
    id_xt_sust = models.IntegerField(primary_key=True)
    
    descripcion = models.CharField(max_length=255)
    riesgo_teratogenico = models.SmallIntegerField()
    estado = models.BooleanField()
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    fecha_ult_mod = models.DateTimeField()
    usuario_ult_mod = models.SmallIntegerField()
    revisado = models.BooleanField()
    consultar = models.BooleanField()
    kairos_sustancia = models.ForeignKey(kairos_sustancia)
    concept_sust_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_sust']
        verbose_name_plural ='extension de sustancias'

## ##-
## table 'xt_mb'
## medicamento basico
## ##-


class xt_mb (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    xt_id_mb = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariocrea_mb')
    fecha_ult_mod = models.DateTimeField(null=False, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_mb')
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default='Unspecified', blank=True)
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified', blank=True)
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified', blank=True)
    concept_vtm_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    rel_xt_sust = models.ManyToManyField(xt_sustancias, through='rel_xt_mb_xt_sust')
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return "%s | %s" % (self.estado, self.descripcion)
    class Meta:
        ordering=['xt_id_mb']
        verbose_name_plural ='medicamento basico (extension)'



class xt_mc (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    OPCIONES_FORMA_FARM = ((1, 'Discreta'),(2,'Continua'),(3,'No Aplica'))
    OPCIONES_PRESCRIPCION = (
         (1,'Invalido para prescribir en Atencion Primaria')
        ,(2,'Nunca valido para prescribir como MC')
        ,(3,'No prescribible como un MC pero es valido como PC')
        ,(4,'No recomendable prescribir como un MC')
        ,(5,'Valido como producto prescribible')
        ,(6,'MC no recomendable para prescribir - marca no bioequivalente')
        ,(7,'MC no recomendable para prescribir - requiere entrenamiento del paciente')
        )
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_mc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False, help_text='Obligatorio')
    med_basico = models.ForeignKey(xt_mb, null=True)
    estado_prescripcion = models.SmallIntegerField(choices=OPCIONES_PRESCRIPCION, null=True, blank=True)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea')
    fecha_ult_mod = models.DateTimeField(null=False, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariomod')
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default='Unspecified')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    tipo_forma_farm = models.SmallIntegerField(choices=OPCIONES_FORMA_FARM, null=False, blank=True)
    tamano_dosis_u = models.IntegerField(null=True, blank=True)
    unidad_dosis_u = models.ForeignKey(xt_unidad_dosis_unitaria, null=True, blank=True)
    unidad_medida_u = models.ForeignKey(xt_unidad_medida_unitaria, null=True, blank=True)
    forma_farmaceutica = models.ForeignKey(xt_formas_farm, null=True, blank=True)
    condicion_venta = models.ForeignKey(xt_condicion_venta, null=True, blank=True)
    concept_vmp_dmd = models.ForeignKey(uk_dmd_conceptos, null=True, blank=True)
    rel_mc = models.ManyToManyField(xt_sustancias, through='rel_mc_sust')
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_mc']
        verbose_name_plural = "medicamento clinico (extension)"


## ##-
## table 'xt_unidad_potencia'
##
## ##-

class xt_unidad_potencia (models.Model):
    id_unidad_potencia = models.SmallIntegerField()
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
## ##-
## table 'rel_mc_sust'
## 
## ##-


class rel_mc_sust (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    id_rel_mc_sust = models.AutoField(primary_key=True)
    id_xt_mc = models.ForeignKey(xt_mc)
    id_xt_sust = models.ForeignKey(xt_sustancias)
    orden = models.SmallIntegerField()
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO)
    potencia = models.IntegerField()
    id_unidad_potencia = models.ForeignKey(xt_unidad_potencia, related_name='unidad potencia')
    partido_por = models.SmallIntegerField(null=True)
    id_unidad_partido_por = models.ForeignKey(xt_unidad_potencia, related_name='unidad partido por')



## ##-
## table 'rel_xt_mb_xt_sust'
## 
## ##-



class rel_xt_mb_xt_sust (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    id_rel_xt_mb_xt_sust = models.AutoField(primary_key=True)
    id_xt_sust = models.ForeignKey(xt_sustancias)
    id_xt_mb = models.ForeignKey(xt_mb)
    orden = models.SmallIntegerField()
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO)



## ##-
## table 'xt_laboratorio'
## laboratorios de la extension
## ##-



class xt_laboratorio (models.Model):
    id_xt_lab = models.IntegerField(primary_key=True)
    
    descripcion = models.SmallIntegerField()
    desc_abrev = models.SmallIntegerField()
    estado = models.BooleanField()
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    fecha_ult_mod = models.DateTimeField()
    usuario_ult_mod = models.SmallIntegerField()
    revisado = models.BooleanField()
    consultar = models.BooleanField()
    clave_lab_kairos = models.ForeignKey(kairos_lab)

    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_lab']
        verbose_name_plural ='laboratorios de la extension'


## ##-
## table 'xt_producto'
## productos de la extension
## ##-



class xt_producto (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_producto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.SmallIntegerField(choices=OPCIONES_ESTADO, null=False, blank=False)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariocrea_producto')
    fecha_ult_mod = models.DateTimeField(null=False, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_producto')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    id_xt_lab = models.ForeignKey(xt_laboratorio)
    clave_prod_kairos = models.ForeignKey(kairos_productos)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_producto']
        verbose_name_plural ='productos de la extension'


## ##-
## table 'xt_gfp'
## grupo de familia de productos de la extension
## ##-



class xt_gfp (models.Model):
    id_xt_gfp = models.IntegerField(primary_key=True)

    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    fecha_ult_mod = models.DateTimeField()
    usuario_ult_mod = models.SmallIntegerField()
    revisado = models.BooleanField()
    consultar = models.BooleanField()
    concept_tfg_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_gfp']
        verbose_name_plural ='grupo de familia de productos de la extension'

## ##-
## table 'xt_fp'
## familia de producto de la extension
## ##-



class xt_fp (models.Model):
    id_xt_fp = models.IntegerField(primary_key=True)
    xtconcepto = models.SmallIntegerField()
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()
    fecha_creacion = models.DateTimeField()
    usuario_creador = models.SmallIntegerField()
    fecha_ult_mod = models.DateTimeField()
    usuario_ult_mod = models.SmallIntegerField()
    revisado = models.BooleanField()
    consultar = models.BooleanField()
    id_producto_xt = models.ForeignKey(xt_producto, null=True)
    concept_tf_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_fp']
        verbose_name_plural ='familia de producto de la extension'




## ##-
## table 'xt_pc'
## productos comerciales de la extension
## ##-

class xt_pc (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_pc = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    descripcion_breviada = models.CharField(max_length=255, verbose_name='Descripcion Abreviada')
    estado = models.SmallIntegerField(choices=OPCIONES_ESTADO, null=False, blank=False)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariocrea_pc')
    fecha_ult_mod = models.DateTimeField(null=False, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_pc')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    id_xt_fp = models.ForeignKey(xt_fp, verbose_name='Familia de Producto')
    id_xt_mc = models.ForeignKey(xt_mc, verbose_name='Medicamento Clinico')
    concept_amp_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    #bioequivalente = models.ManyToManyField('self', through='xt_bioequivalente', symmetrical=False)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_pc']
        verbose_name_plural ='productos comerciales (extension)'




## ##-
## table 'xt_unidad_medida_cant'
## unidad de medida de cantidad de la extension
## ##-



class xt_unidad_medida_cant (models.Model):
    id_unidad_medida_cant = models.IntegerField(primary_key=True)
    
    descripcion = models.CharField(max_length=255)

    def __unicode__(self):
        return self.descripcion
    observacion = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        ordering=['id_unidad_medida_cant']
        verbose_name_plural ='unidad de medida de cantidad de la extension'

## ##-
## table 'xt_mcce'
## medicamento clinico con envase (extension)
## ##-


class xt_mcce (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_mcce = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariocrea_mcce')
    fecha_ult_mod = models.DateTimeField(null=False, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=False, blank=False, editable=False, related_name='usuariomod_mcce')
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default='Unspecified')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    id_xt_mc = models.ForeignKey(xt_mc, verbose_name='Medicamento Clinico')
    cantidad = models.IntegerField()
    unidad_medida_cant = models.ForeignKey(xt_unidad_medida_cant)
    concept_vmpp_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_mcce']
        verbose_name_plural ='medicamento clinico con envase (extension)'


## ##-
## table 'xt_pcce'
## productos comerciales con envase de la extension
## ##-



class xt_pcce (models.Model):
    OPCIONES_ESTADO = ((1, 'No Vigente'),(0, 'Vigente'))
    OPCIONES_BOOL = ((1,'Si'),(0,'No'))
    id_xt_pcce = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    desc_abreviada = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    usuario_creador = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariocrea_pcce')
    fecha_ult_mod = models.DateTimeField(null=False, auto_now=True)
    usuario_ult_mod = models.ForeignKey(User, null=True, blank=True, editable=False, related_name='usuariomod_pcce')
    estado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_ESTADO, null=False, default='Unspecified')
    revisado = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    consultar = models.PositiveSmallIntegerField(max_length=1,choices=OPCIONES_BOOL, default='Unspecified')
    id_xt_pc = models.ForeignKey(xt_pc, verbose_name= 'Producto Comercial')
    id_xt_mcce = models.ForeignKey(xt_mcce, verbose_name='Medicamento Clinico Con Envase')
    gtin_gs1 = models.BigIntegerField()
    concept_ampp_dmd = models.ForeignKey(uk_dmd_conceptos, null = True, blank=True)
    id_presentacion_kairos = models.ForeignKey(kairos_presentaciones, verbose_name='Presentacion Kairos')
    observacion = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering=['id_xt_pcce']
        verbose_name_plural ='productos comerciales con envase (extension)'




class xt_bioequivalente(models.Model):
    id_xt_bioequivalente = models.AutoField(primary_key=True)
    referencia = models.ForeignKey(xt_pc, related_name='referencia')
    bioequivalente = models.ForeignKey(xt_pc, related_name='equivalente')
    def __unicode__(self):
        return self.id_xt_bioequivalente