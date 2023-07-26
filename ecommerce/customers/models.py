from django.db import models
from django.contrib.auth import models as user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AuthenticatedCustomer(user_model.User):
    """
    a user who already authenticated
    """
    date_deleted = models.DateTimeField(_("Date Deleted"), null=True)
    date_updated = models.DateTimeField(_("Date Updated", auto_now=True))
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        app_label = 'customers'
        verbose_name = _("old customer")
        ordering = ["first_name", "last_name"]







