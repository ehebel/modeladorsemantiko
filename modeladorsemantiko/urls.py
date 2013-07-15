from django.conf.urls import patterns, include, url
from django.views import generic

import autocomplete_light
# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

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
    (r'^modelador/$', generic.TemplateView.as_view(template_name='index.html'))
)



from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()