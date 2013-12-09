# Create your views here.
from django.shortcuts import render_to_response
from efectorescas.models import *


def lista_areas(solicitud):
    areas = cas_area.objects.order_by('id')
    conceptos = concepto.objects.order_by('id').filter(pedible__exact=1)
    descripciones = descripcion.objects.order_by('id')
    return render_to_response('efectores.html'
        ,{'listado_areas':areas,
          'listado_fsn': conceptos,
          'listado_descripciones':descripciones,
        })

