from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Member


@admin.register(Member)
class CustomUserAdmin(UserAdmin):
    model = Member

    list_display = (
        'username', 'full_name',
        'is_active', 'sex',
        'profile_photo')

    list_filter = ('is_staff', 'is_active', 'sex')

    fieldsets = (
        (None, {'fields': (
            'username', 'first_name', 'last_name',
            'password', 'sex', 'profile_photo',
        )}),
        ('Permissions', {'fields': (
            'is_staff', 'is_active',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'last_name',
                'sex', 'profile_photo',
                'password1', 'password2',
                'is_staff', 'is_active',
            ),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ()
