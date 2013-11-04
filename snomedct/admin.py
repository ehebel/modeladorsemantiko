import autocomplete_light
autocomplete_light.autodiscover()
from django.contrib import admin
admin.autodiscover()
from snomedct.models import sct_concept, sct_description, sct_relationship


class conceptAdminInLine(admin.TabularInline):
    model = sct_concept
    form = autocomplete_light.modelform_factory(sct_concept)

class relationshipAdminInline(admin.TabularInline):
    model = sct_relationship
    form = autocomplete_light.modelform_factory(sct_relationship)
    readonly_fields = ['relationshipid',]
    fk_name = 'conceptid2'

class conceptAdmin(admin.ModelAdmin):
    search_fields = ['conceptid','fullyspecifiedname']
    list_filter = ['conceptstatus']
    inlines = [relationshipAdminInline]

admin.site.register(sct_concept,conceptAdmin)


class descriptionAdmin(admin.ModelAdmin):
    search_fields = ['term']
    list_filter = ['descriptionstatus','initialcapitalstatus','descriptiontype']
    list_display = ['descriptionid','term','conceptid']
    form = autocomplete_light.modelform_factory(sct_description)
    #inlines = [conceptAdminInLine]
admin.site.register(sct_description,descriptionAdmin)

admin.site.register(sct_relationship)
__author__ = 'ehebel'
