from django.contrib import admin

from apps.timetable.models import Job, WeekDay, WorkTime


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ("title", "weekend")


@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    pass
