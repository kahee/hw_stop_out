from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cralwer import get_episode_list
from webtoon.models import Webtoon, Episode


def webtoon_list(request):
    # 저장된 웹툰 리스트를 보여줌
    webtoons = Webtoon.objects.all()
    context = {
        'webtoons': webtoons
    }
    return render(request, 'webtoon/webtoon_list.html', context)


def webtoon_detail(request, pk):
    webtoon = Webtoon.objects.get(pk=pk)

    # webtoon_id 로 get_episode_list 실행
    results = get_episode_list(webtoon.webtoon_id, 1)
    # 각 딕셔너리의 key로 value 지
    for result in results:
        episode_id = result.get('episode_id')
        title = result.get('title')
        rating = result.get('rating')
        created_date = result.get('created_date')

        # 크롤링한 데이터 Episode 테이블에 저장
        episode = Episode.objects.create(
            webtoon=Webtoon.objects.get(pk=pk),
            title=title,
            episode_id=episode_id,
            rating=rating,
            created_date=created_date)
        episode.save()

    context = {
        'webtoon': webtoon

    }

    return render(request, 'webtoon/webtoon_detail.html', context)
