from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.views.generic import DetailView
from django.views.generic.base import View
from django.template import RequestContext
from django.core.paginator import Paginator
from modeladorFarmacos.models import xt_mc,xt_pc,xt_pcce, xt_mcce


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        med_clinicos = xt_mc.objects.filter(descripcion__icontains=q,estado=0).order_by('descripcion')
        return render(request, 'search_results.html',
            {'medicmentos': med_clinicos, 'query': q})
    else:
        return HttpResponse('Favor elija un termino valido.')

def selec_medclin(solicitud, medclinid):
    try:
        medclinid = int(medclinid)
    except ValueError:
        raise Http404
    medclinicos = xt_mc.objects.order_by('id_xt_mc').get(id_xt_mc=medclinid)
    prodcomercial = medclinicos.xt_pc_set.all()
    return render_to_response('seleccion_medclin.html'
        ,{'listado_mc': medclinicos
        ,'listado_pc': prodcomercial
          })


def lista_mc(solicitud):
    mc = xt_mc.objects.order_by('descripcion').filter(descripcion__contains='Valsart')
    pc = xt_pc.objects.order_by('id_xt_pc')
    pcce = xt_pcce.objects.order_by('id_xt_pcce')
    mcce = xt_mcce.objects.order_by('id_xt_mcce')
    return render_to_response('catalogo.html'
        ,{'listado_mc':mc,
          'listado_pc': pc,
          'listado_pcce':pcce,
          'listado_mcce':mcce,
          })






