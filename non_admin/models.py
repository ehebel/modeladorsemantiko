from django.db import models
from django.core.urlresolvers import reverse


class Widget(models.Model):
    city = models.ForeignKey('modeladorFarmacos2.xt_pc', null=True, blank=True)
    users = models.ManyToManyField('auth.user', blank=True)

    def get_absolute_url(self):
        return reverse('non_admin:widget_update', args=(self.pk,))
