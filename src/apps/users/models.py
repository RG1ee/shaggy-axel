from apps.users.managers import MemberManager

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


SEX_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Member(AbstractUser):

    objects = MemberManager()

    REQUIRED_FIELDS = []

    sex = models.CharField(
        'Пол', max_length=6,
        choices=SEX_CHOICES, default='Male')
    profile_photo = models.ImageField(
        'Фото', upload_to='users/profile_photo',
        null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username
