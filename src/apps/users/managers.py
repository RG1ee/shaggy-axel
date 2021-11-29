from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class MemberManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Create and save a User with the given data.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        extra_fields.setdefault('is_active', True)

        member = self.model(username=username, **extra_fields)
        member.set_password(password)
        member.save()
        return member

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)
