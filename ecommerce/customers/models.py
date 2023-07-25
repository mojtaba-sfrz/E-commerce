from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AuthenticatedCustomer(models.User):
    """
    a user who already authenticated
    """
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _("old customer")
        ordering = ["first_name", "last_name"]





