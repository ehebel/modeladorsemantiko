from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import  HttpResponseRedirect

from django.shortcuts import  render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from modeladorFarmacos2.models import kairos_productos\
    , kairos_presentaciones, xt_mc, xt_pcce, xt_bioequivalente

from modeladorFarmacos2.forms import pcceForm


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args,**kwargs):
        return super(LoggedInMixin, self).dispatch(*args,**kwargs)


def create(request):
    if request.POST:
        form = pcceForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')

    else:
        form = pcceForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('modeladorFarmacos/crear_pcce.html', args)

class VistaListaPCCECreadores(LoggedInMixin,ListView):
    model = xt_pcce
    template_name = 'modeladorFarmacos2/creadores_pcce.html'

    def get_queryset(self):
        return xt_pcce.objects.filter(revisado__exact=0).order_by('usuario_creador')

class VistaUsuarioCreadorPCCE(LoggedInMixin,ListView):
    context_object_name = 'lista_pcce_por_usuario'
    template_name = 'modeladorFarmacos2/pcce_por_usuario.html'

    def get_queryset(self):
        usuario_creador = get_object_or_404(User, id__iexact=self.args[0])
        return xt_pcce.objects.filter(usuario_creador=usuario_creador, revisado__exact=0).order_by('descripcion')


class VistaListaPCCE(LoggedInMixin, ListView):
    model = xt_pcce
    template_name = 'modeladorFarmacos/pcce_por_revisar.html'

    def get_queryset(self):

        return xt_pcce.objects.filter(revisado__exact=0)



class VistaCrearPCCE(CreateView):
    model = xt_pcce
    template_name = 'modeladorFarmacos/pcce_editar.html'

    def get_success_url(self):
        return reverse('pcce-lista')


class VistaEditarPCCE(LoggedInMixin,UpdateView):

    model = xt_pcce
    template_name = 'modeladorFarmacos/pcce_editar.html'



    def get_success_url(self):
        return reverse('pcce_lista')

    def get_context_data(self, **kwargs):

        context = super(VistaEditarPCCE, self).get_context_data(**kwargs)
        context['action'] = reverse('pcce_editar',
            kwargs={'pk': self.get_object().id_xt_pcce})

        return context




class  VistaPCCE(DetailView):
    model = xt_pcce
    template_name = 'modeladorFarmacos/pcce_detalle.html'




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
    inner_qs = xt_bioequivalente.objects.values_list('referencia', flat=True).distinct()

    mc_list = xt_mc.objects.order_by('descripcion').filter(

        xt_pc__id_xt_pc__in = inner_qs ,

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
        ,{'pendientes_mc':mc
        ,'bioeq_referentes':inner_qs},
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
