from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
#from django.http import HttpResponse, Http404
#from django.views.generic import DetailView
#from django.views.generic.base import View
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, InvalidPage
import operator
from django.views.generic import ListView, UpdateView

from modeladorFarmacos2.models import kairos_productos\
    , kairos_presentaciones, xt_mc, xt_pcce, xt_bioequivalente

# Create your views here.
class VistaListaPCCE(ListView):
    model = xt_pcce
    template_name = 'modeladorFarmacos/pcce_por_revisar.html'

    def get_queryset(self):

        return xt_pcce.objects.order_by('usuario_ult_mod','-fecha_ult_mod').filter(usuario_ult_mod__groups__id__exact=4, estado__exact=0)


class VistaEditarPCCE(UpdateView):
    model = xt_pcce
    template_name = 'modeladorFarmacos/pcce_editar.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(VistaEditarPCCE, self).get_context_data(**kwargs)
        context['action'] = reverse('pcce-edit',
            kwargs={'pk': self.get_object().id})

        return context



def modeladorescas(solicitud):
    pcce_list = xt_pcce.objects.order_by('usuario_ult_mod','-fecha_ult_mod').filter(usuario_ult_mod__groups__id__exact=4)

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
    inner_qs = xt_bioequivalente.objects.values('referencia').distinct()
    mc_list = xt_mc.objects.order_by('descripcion').filter(

        xt_pc__id_xt_pc__in= inner_qs ,

        estado__exact=0,
    ).distinct()

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


def kairos2(request):
    kpres_list = kairos_presentaciones.objects.filter(medio__in=['Comp. '
            ,'Caps. '
            ,'Grag. '
            ,'Tab.'
        ]
        ).exclude(estado__icontains='B').order_by('claveproducto__descripcion'
            , 'concentracion'
            ,'cantidadenvase'
        ).distinct().all()

    paginator = Paginator(kpres_list, 275)

    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        kairos_pres = paginator.page(page)
    except(EmptyPage, InvalidPage):
        kairos_pres = paginator.page(paginator.num_pages)


    return render_to_response('modeladorFarmacos/listado_kairos.html'
        ,{'kpres_kairos':kairos_pres},
        context_instance=RequestContext(request))
