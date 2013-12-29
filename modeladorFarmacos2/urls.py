from django.conf.urls import patterns, url
from django.views import generic

from forms import pcceForm
from models import xt_pcce


urlpatterns = patterns('',
    url(r'add/$', generic.CreateView.as_view(
        model=xt_pcce, form_class=pcceForm)),
    url(r'(?P<pk>\d+)/update/$', generic.UpdateView.as_view(
        model=xt_pcce, form_class=pcceForm), name='pcce-detalle'),
)

__author__ = 'ehebel'
