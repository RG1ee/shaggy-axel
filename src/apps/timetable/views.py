from django.shortcuts import render


def timetable_render_view(request):
    return render(request, template_name="timetable/timetable.html")
