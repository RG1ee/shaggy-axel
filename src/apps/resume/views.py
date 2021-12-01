from django.http import FileResponse, Http404


def resume_view(request):
    try:
        return FileResponse(open('my_resume.pdf', 'rb'))
    except FileNotFoundError:
        raise Http404()
