from django.shortcuts import render, render_to_response
#from django.http import HttpResponse, Http404
#from django.views.generic import DetailView
#from django.views.generic.base import View
from django.template import RequestContext
from django.core.paginator import Paginator

from modeladorFarmacos2.models import kairos_productos

# Create your views here.
def kairos(request):
    kairos_list = kairos_productos.objects\
        .filter(kairos_presentaciones__medio__in=['Comp.','Caps.'])\
        .order_by('descripcion')\
        .exclude(kairos_presentaciones__estado__exact='B')\
        .all()
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