from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from ecommerce.catalogue.models import Product
from ecommerce.suppliers.models import Supplier


class StockRecord(models.Modle):
    date_created = models.DateTimeField(_("Date created"),
                                        auto_now_add=True)

    date_updated = models.DateTimeField(_("Date Updated",
                                          auto_now=True))

    date_deleted = models.DateTimeField(_("Date Deleted"),
                                        null=True)

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="Stock record of")

    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE,
        related_name="Seller of"
    )

    price = models.DecimalField(
        _("Price"), decimal_places=2, max_digits=12,
        blank=True, null=True)

    num_in_stock = models.PositiveIntegerField(
        _("Number in stock"), blank=True, null=True)

    num_allocated = models.IntegerField(
        _("Number allocated"), blank=True, null=True,
        help_text="Number of products allocated to order")

    low_stock_threshold = models.PositiveIntegerField(
        _("Low Stock Threshold"), blank=True, null=True,
        help_text="""Threshold for low-stock alerts.  When
                  stock goes beneath this threshold an 
                  alert is triggered so warehouse managers
                  can order more.""")

    class Meta:
        verbose_name = _("Stock record")
        verbose_name_plural = _("Stock records")
