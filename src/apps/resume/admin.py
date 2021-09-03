from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Education, Job, Resume, Skill, SkillCategory


class EducationInline(admin.TabularInline):
    model = Education
    fields = (
        'school', 'course',
        'start_date', 'end_date')

    def get_extra(self, request, obj=None, **kwargs):
        return 1


class JobInline(admin.TabularInline):
    model = Job
    fields = (
        'position', 'company',
        'stack',
        'start_date', 'end_date')

    def get_extra(self, request, obj=None, **kwargs):
        return 1


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm

    list_display = (
        '__str__', 'position',
    )

    fieldsets = (
        (None, {'fields': (
            'applicant',
            'about',
            'position',
            'skills',
        )}),
    )
    add_fieldsets = (
        (None, {'fields': (
            'applicant',
            'about',
            'position',
            'skills',
        )}),
    )
    search_fields = (
        'applicant', 'position',
    )
    ordering = (
        'applicant',
    )
    inlines = [
        JobInline,
        EducationInline,
    ]
    filter_horizontal = ()


admin.site.register(Skill)
admin.site.register(SkillCategory)
