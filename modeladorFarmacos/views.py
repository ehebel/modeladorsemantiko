# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from modeladorFarmacos.models import xt_mc


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        med_clinicos = xt_mc.objects.filter(descripcion__icontains=q).order_by('med_basico')
        return render(request, 'search_results.html',
            {'medicmentos': med_clinicos, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

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