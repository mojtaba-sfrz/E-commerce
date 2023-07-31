from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy


class Order(models.Model):
    """
    The main order model
    """
    number = models.CharField(
        _("Order number"), max_length=128, unique=True)

    basket = models.ForeignKey(
        'basket.Basket', verbose_name=_("Basket"),
        null=True, blank=True, on_delete=models.SET_NULL)

    user = models.ForeignKey(
        'customer.AuthenticatedCustomer', related_name='orders', null=True, blank=True,
        verbose_name=_("User"), on_delete=models.SET_NULL)

    address = models.ForeignKey(
        'order.BillingAddress', null=True, blank=True,
        verbose_name=_("Billing Address"),
        on_delete=models.SET_NULL)

    total_incl_tax = models.DecimalField(
        _("Order total (inc. tax)"), decimal_places=2, max_digits=12)
    total_excl_tax = models.DecimalField(
        _("Order total (excl. tax)"), decimal_places=2, max_digits=12)

    date_placed = models.DateTimeField(db_index=True)

    guest_email = models.EmailField(_("Guest email address"), blank=True)

    class Meta:
        app_label = 'order'
        ordering = ['-date_placed']
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        Indexes = [
            models.Index("number", "date_placed")
        ]
