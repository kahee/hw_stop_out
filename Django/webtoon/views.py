from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from webtoon.models import Webtoon


def webtoon_list(request):
    webtoons = Webtoon.objects.all()
    context = {
        'webtoons': webtoons
    }

    return render(request,'webtoon/webtoon_list.html',context)
