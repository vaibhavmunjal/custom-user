import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator


from .managers import UserManager


def _Profile_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('profile_pictures/', filename)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Completely Extend the Base User
    """
    first_name = models.CharField(_("First Name"), max_length=50)

    last_name = models.CharField(_("Last Name"), max_length=50)

    mobile_number = models.CharField(_("Mobile Number"), max_length=16)

    email = models.EmailField(_("Email"), max_length=50, unique=True)

    gender = models.CharField(_("Gender"), max_length=50)

    dob = models.DateField(_("Birth Date"), null=True, blank=True)

    address = models.CharField(_("Address"),
                            max_length=100,
                            null=True,
                            blank=True)

    profile_picture = models.ImageField(_("Profile Picture"),
                                    upload_to=_Profile_image_path,
                                    null=True,
                                    blank=True)

    city = models.CharField(_("City"),
                        max_length=50,
                        null=True,
                        blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Is User belongs to staff')
    )

    is_active = models.BooleanField(
        _('active status'),
        default=True,
        help_text=_('Should User be treated as Active')
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
    ]
