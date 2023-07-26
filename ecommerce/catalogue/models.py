from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from ecommerce.order.models import Basket


class Product(models.Model):
    """
    this model records product information
    """

    title = models.CharField(pgettext_lazy('Product title', 'Title'),
                             max_length=255, blank=True)
    description = models.TextField(_('Description'), blank=True)
    rating = models.FloatField(_('Rating'), null=True, editable=False)
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated", auto_now=True))
    added = models.ForeignKey(
        Basket,
        null=True,
        related_name='added in',
        on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-date_created']
        app_label = 'catalogue'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):

        return self.title

