from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from webtoon.models import Webtoon


def webtoon_list(request):
    webtoon = Webtoon.objects.all()
    context = {
        'webtoon': webtoon
    }

    return HttpResponse(webtoon)
