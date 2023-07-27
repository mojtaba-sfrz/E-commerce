from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from ecommerce.suppliers.models import Supplier
from ecommerce.customers.models import AuthenticatedCustomer
import re
from django.core import exceptions


class Address(models.Model):

    """"
    this is the address model. this class maintains both customers and sellers addresses
    """

    MR, MISS, MRS, MS, DR = ('Mr', 'Miss', 'Mrs', 'Ms', 'Dr')
    TITLE_CHOICES = (
        (MR, _("Mr")),
        (MISS, _("Miss")),
        (MRS, _("Mrs")),
        (MS, _("Ms")),
        (DR, _("Dr")),
    )
    POSTCODES_REGEX = r'^[0-9]{5}-[0-9]{5}$'

    title = models.CharField(
        pgettext_lazy("Treatment Pronouns for the customer", "Title"),
        max_length=64, choices=TITLE_CHOICES, blank=True)
    first_name = models.CharField(_("First name"), max_length=255, blank=True)
    last_name = models.CharField(_("Last name"), max_length=255, blank=True)
    state = models.CharField(_("State/County"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=255, blank=True)
    line1 = models.CharField(_("First line of address"), max_length=255)
    line2 = models.CharField(
        _("Second line of address"), max_length=255, blank=True)
    line3 = models.CharField(
        _("Third line of address"), max_length=255, blank=True)
    postcode = models.CharField(
        _("Post/Zip-code"), max_length=64, blank=True)

    customer = models.ForeignKey(AuthenticatedCustomer,
                                 on_delete=models.CASCADE,
                                 related_name="The address of",
                                 )
    supplier = models.ForeignKey(Supplier,
                                 on_delete=models.CASCADE,
                                 related_name="The address of",
                                 )

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def ensure_postcode_is_valid(self):
        postcode = self.postcode.upper().replace(' ', '')
        regex = self.POSTCODES_REGEX
        if not re.match(regex, postcode):
            msg = _("The postcode '%(postcode)s' is not valid ")
            raise exceptions.ValidationError(
                {'postcode': [msg]})
