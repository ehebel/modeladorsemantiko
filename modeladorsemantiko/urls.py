from django.conf.urls import patterns, include, url
from django.views import generic

import autocomplete_light
# import every app/autocomplete_light_registry.py
from modeladorFarmacos2.forms import pcceForm
from modeladorFarmacos2.models import xt_pcce
from non_admin.forms import WidgetForm
from non_admin.models import Widget

autocomplete_light.autodiscover()
from django.contrib import admin
admin.autodiscover()

from efectorescas.views import  lista_areas
from modeladorFarmacos.views import search, selec_medclin,lista_mc
from modeladorFarmacos2.views import modeladorescas,pendientes,kairos,kairos2
import modeladorFarmacos2.views
from modeladorFarmacos2.views import pcceForm



#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'modeladorsemantiko.views.home', name='home'),
#    # url(r'^modeladorsemantiko/', include('modeladorsemantiko.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^/doc/', include('django.contrib.admindocs.urls')),
#
#    # Uncomment the next line to enable the admin:
#    url(r'^', include(admin.site.urls)),
#    url(r'^autocomplete/', include('autocomplete_light.urls')),
#)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^modelador/admin/', include(admin.site.urls)),

    #url(r'support_sandino/', include('support_sandino.urls')),
    #url(r'^non_admin/', include('non_admin.urls', namespace='non_admin')),
    #url(r'^non_admin_add_another/', include('non_admin_add_another.urls',
    #    namespace='non_admin_add_another')),
    url(r'^double_loading/', generic.TemplateView.as_view(
        template_name='double_loading.html')),
    url(r'^modelador/autocomplete/', include('autocomplete_light.urls')),
    #url(r'^navigation/', include('navigation_autocomplete.urls')),
    #url(r'^default_template/', include('default_template_autocomplete.urls')),
    url(r'^cities_light/', include('cities_light.contrib.restframework')),
    #url(r'^hvad_autocomplete/', include('hvad_autocomplete.urls',
    #    namespace='hvad_autocomplete')),
    #url(r'^inlines_outside_admin/', include('inlines_outside_admin.urls',
    #    namespace='inlines_outside_admin')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^just_javascript/$', generic.TemplateView.as_view(
        template_name='just_javascript.html')),

    (r'^modelador/$', generic.TemplateView.as_view(template_name='index.html')),


    url(r'^modelador/login/$', 'django.contrib.auth.views.login'),
    url(r'^modelador/logout/$', 'django.contrib.auth.views.logout'),


    url(r'^modelador/xt_pcce/lista_usuarios/$', modeladorFarmacos2.views.VistaListaPCCECreadores.as_view(),
        name='creadores_lista',),

    url(r'^modelador/xt_pcce/lista_usuarios/(\w+)/$', modeladorFarmacos2.views.VistaUsuarioCreadorPCCE.as_view()),



    url(r'^modelador/xt_pc/lista_usuarios/$', modeladorFarmacos2.views.VistaListaPCCreadores.as_view(),
        name='creadores_lista',),

    url(r'^modelador/xt_pc/lista_usuarios/(\w+)/$', modeladorFarmacos2.views.VistaUsuarioCreadorPC.as_view()),



    url(r'^modelador/lista_pcce/$', modeladorFarmacos2.views.VistaListaPCCE.as_view(),
        name='pcce_lista',),



    url(r'^modelador/lista_pcce/nuevo/$', modeladorFarmacos2.views.VistaCrearPCCE.as_view(),
        name='pcce_nuevo',),

    url(r'^modelador/lista_pcce/editar/(?P<pk>\d+)/$'
        , modeladorFarmacos2.views.VistaEditarPCCE.as_view(
            model=xt_pcce
            ,form_class=pcceForm)
            , name='pcce_editar'),



    url(r'^modelador/lista_pcce/(?P<pk>\d+)/$', modeladorFarmacos2.views.VistaPCCE.as_view(),
        name='pcce_detalle',),


    url(r'^modelador/crear_pcce/$'
#        , 'modeladorFarmacos2.views.create'
        ,  generic.CreateView.as_view(
            model=xt_pcce, form_class=pcceForm
        )),


    (r'^modelador/CAS/efectores/$', lista_areas),
    (r'^modelador/CAS/modeladores/$', modeladorescas),

    (r'^modelador/search-form/$', generic.TemplateView.as_view(template_name='search_form.html')),
    (r'^modelador/search/$', search),
    (r'^modelador/seleccion_medclin/(\d{1,4})/$', selec_medclin ),
    (r'^modelador/catalogo/$', lista_mc),
    (r'^modelador/pendientes/$', pendientes),
    (r'^modelador/kairos/$', kairos2),



    url(r'^modelador/non_admin/', include('non_admin.urls', namespace='non_admin')),

)



from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()