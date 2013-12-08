__author__ = 'ehebel'
from modeladorFarmacos2.models import *
from django.contrib import admin


current_app = models.get_app(__package__)
for model in models.get_models(current_app):
    admin.site.register(model, admin.ModelAdmin)