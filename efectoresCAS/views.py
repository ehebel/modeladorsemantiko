# Create your views here.
from django.shortcuts import render_to_response
from efectoresCAS.models import *


def lista_areas(solicitud):
    areas = cas_areas.objects.order_by('id')
    conceptos = concepto.objects.order_by('id')
    descripciones = descripcion.objects.order_by('id')
    return render_to_response('efectores.html'
        ,{'listado_areas':areas,
          'listado_fsn': conceptos,
          'listado_descripciones':descripciones,
        })

