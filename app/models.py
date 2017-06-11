from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),
                              unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              })

    USERNAME_FIELD = 'email'
    objects = BaseUserManager()

    def __str__(self):
        return self.email

    is_staff = models.BooleanField(_('staff status'),
                                   default=True,
                                   help_text=_('Designates whether the user can log into this admin site.'))

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
