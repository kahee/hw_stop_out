from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from webtoon.models import Webtoon


def webtoon_list(request):
    # 저장된 웹툰 리스트를 보여줌
    webtoons = Webtoon.objects.all()
    context = {
        'webtoons': webtoons
    }
    return render(request, 'webtoon/webtoon_list.html', context)


def webtoon_detail(request, pk):
    episode = Webtoon.objects.get(pk=pk)

    return HttpResponse(episode)
