from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class MemberManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given data.
        """

        if not username or not email:
            raise ValueError(_('The Username must be set'))
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        member = self.model(username=username, email=email, **extra_fields)
        member.set_password(password)
        member.save()
        return member

    def create_superuser(self, username, email, password, **extra_fields):
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
        return self.create_user(username, email, password, **extra_fields)
