from django.db import models
from django.utils.translation import gettext_lazy as _
from ecommerce.customers.models import AuthenticatedCustomer


class Basket(models.Model):
    owner = models.OneToOneField(
        AuthenticatedCustomer,
        null=True,
        related_name='basket of',
        on_delete=models.CASCADE,
        verbose_name=_("Owner"))

    OPEN, SAVED, FROZEN, SUBMITTED = (
        "Open", "Saved", "Frozen", "Submitted")
    STATUS_CHOICES = (
        (OPEN, _("Open - currently active")),
        (SAVED, _("Saved - for items to be purchased later")),
        (FROZEN, _("Frozen - the basket cannot be modified")),
        (SUBMITTED, _("Submitted - order is in process")),
    )
    status = models.CharField(
        _("Status"), max_length=128, default=OPEN, choices=STATUS_CHOICES)

    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)
    date_submitted = models.DateTimeField(_("Date submitted"), null=True, blank=True)

    class Meta:
        app_label = 'order'
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')
