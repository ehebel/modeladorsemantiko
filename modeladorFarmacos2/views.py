from django.shortcuts import render, render_to_response
#from django.http import HttpResponse, Http404
#from django.views.generic import DetailView
#from django.views.generic.base import View
from django.template import RequestContext
from django.core.paginator import Paginator
import operator

from modeladorFarmacos2.models import kairos_productos, kairos_presentaciones, xt_mc, xt_pcce

# Create your views here.

def modeladorescas(solicitud):
    pcce_list = xt_pcce.objects.order_by('usuario_creador','-fecha_creacion','usuario_ult_mod','-fecha_ult_mod').filter(usuario_ult_mod__groups__id__exact=4)

    paginator = Paginator(pcce_list, 100)

    try:
        page = int(solicitud.GET.get('page','1'))
    except:
        page = 1

    try:
        pcce = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pcce = paginator.page(paginator.num_pages)


    return render_to_response('modeladorFarmacos/resultados.html'
        ,{'modelados_pcce':pcce},
        context_instance=RequestContext(solicitud))

def pendientes(solicitud):
    mc_list = xt_mc.objects.order_by('descripcion').filter(
        #        descripcion__contains=u'cido acetilsalic',
        estado__exact=0,
    ) #.exclude(xt_pc__xt_pcce__id_xt_mcce__tipo__in=[1,2,4,5])

    paginator = Paginator(mc_list, 200)

    try:
        page = int(solicitud.GET.get('page','1'))
    except:
        page = 1

    try:
        mc = paginator.page(page)
    except(EmptyPage, InvalidPage):
        mc = paginator.page(paginator.num_pages)


    return render_to_response('listado_trabajo.html'
        ,{'pendientes_mc':mc},
        context_instance=RequestContext(solicitud))


def kairos(request):
    kairos_list = kairos_productos.objects.filter(kairos_presentaciones__medio__in=['Comp.','Caps.']).order_by('clave').distinct().all()
#
#    kairos_ids = kairos_presentaciones.objects.filter(medio__in=['Comp.','Caps.']).exclude(estado__exact='B').values_list('claveproducto_id',flat=True)
#    kairos_list = kairos_productos.objects.filter(clave__in=kairos_ids).order_by('clave').all()
#    kairos_list = kairos_productos.objects.filter(kairos_presentaciones__estado__exact='B').order_by('clave').distinct()

#    kairos_ids = [m.clave for m in kairos_productos if
#                    reduce(operator.and_,[c.medio for c in m.kairos_presentaciones_set.all()])]
#    kairos_list = kairos_productos.objects.filter(clave__in=kairos_ids)

    paginator = Paginator(kairos_list, 275)

    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        kairos_prod = paginator.page(page)
    except(EmptyPage, InvalidPage):
        kairos_prod = paginator.page(paginator.num_pages)


    return render_to_response('listado_kairos.html'
        ,{'pendientes_kairos':kairos_prod},
        context_instance=RequestContext(request))

