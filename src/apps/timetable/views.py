from django.shortcuts import render


def timetable_render_view(request):
    work_time_list = (
        "7.00 - 8.00", "8.00 - 9.00", "9.00 - 10.00",
        "10.00 - 11.00", "11.00 - 12.00", "12.00 - 13.00",
        "13.00 - 14.00", "14.00 - 15.00", "15.00 - 16.00",
        "16.00 - 17.00", "17.00 - 18.00", "18.00 - 19.00",
        "19.00 - 20.00", "20.00 - 21.00", "21.00 - 22.00")
    data = {
        "work_time_list": work_time_list,
    }
    return render(request, "timetable/timetable.html", data)
