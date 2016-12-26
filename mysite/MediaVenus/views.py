from django.http import HttpResponse

from .models import MediaVenus


def index():
    # latest_mediavenus_list = MediaVenus.objects
    return HttpResponse("MediaVenus MediaVenus MediaVenus")
#     return HttpResponse(latest_mediavenus_list)


# def index(request):
#     template_name = 'MediaVenus/mediavenus.html'
#     context_object_name = 'latest_mediavenus_list'
#
#     def get_queryset(self):
#         return MediaVenus.objects


