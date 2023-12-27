from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext as _
from apps.account.managers.user import CustomUserManager
from django.contrib.auth.models import PermissionsMixin


class BlogUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email    = models.EmailField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD="username"
    REQUIRED_FIELDS =["email"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.get_username()
    
    class Meta:
        verbose_name = _("Blog User")
        verbose_name_plural = _("Blog Users")
        default_related_name = "blog_users"

        