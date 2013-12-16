from django.shortcuts import render, render_to_response
#from django.http import HttpResponse, Http404
#from django.views.generic import DetailView
#from django.views.generic.base import View
from django.template import RequestContext
from django.core.paginator import Paginator
import operator

from modeladorFarmacos2.models import kairos_productos, kairos_presentaciones

# Create your views here.

def kairos(request):
    kairos_list = kairos_productos.objects.filter(kairos_presentaciones__medio__in=['Comp.','Caps.']).order_by('clave').distinct().all()
#
#    kairos_ids = kairos_presentaciones.objects.filter(medio__in=['Comp.','Caps.']).exclude(estado__exact='B').values_list('claveproducto_id',flat=True)
#    kairos_list = kairos_productos.objects.filter(clave__in=kairos_ids).order_by('clave').all()
#    kairos_list = kairos_productos.objects.filter(kairos_presentaciones__estado__exact='B').order_by('clave').distinct()

#    kairos_ids = [m.clave for m in kairos_productos if
#                    reduce(operator.and_,[c.medio for c in m.kairos_presentaciones_set.all()])]
#    kairos_list = kairos_productos.objects.filter(clave__in=kairos_ids)

    paginator = Paginator(kairos_list, 200)

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


#make_ids = MakeContent.objects.filter(published=True).values_list('make_id', flat=True)
#makes = Make.objects.filter(id__in=make_ids)
#
#import operator
#make_ids = [m.id for m in makes if
#            reduce(operator.and_, [c.published for c in m.makecontent_set.all()] )
#]
#makes_query = Make.objects.filter(id__in=make_ids)