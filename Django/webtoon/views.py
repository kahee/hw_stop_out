from django.shortcuts import render

# Create your views here.
from cralwer import get_episode_list
from webtoon.models import Webtoon, Episode


def webtoon_list(request):
    # 저장된 웹툰 에피소드 리스트 출력
    webtoons = Webtoon.objects.all()
    context = {
        'webtoons': webtoons
    }
    return render(request, 'webtoon/webtoon_list.html', context)


def webtoon_detail(request, pk):
    # 웹툰 제목 클릭시 웹툰 에피소드 크롤링
    webtoon = Webtoon.objects.get(pk=pk)

    # webtoon_id 로 get_episode_list 실행
    results = get_episode_list(webtoon.webtoon_id)

    # 각 딕셔너리의 key로 value
    for result in results:
        episode_id = result.get('episode_id')
        title = result.get('title')
        rating = result.get('rating')
        created_date = result.get('created_date')

        # 데이터 중복 여부 체크
        if not Episode.objects.filter(episode_id=episode_id, webtoon=pk).exists():
            # 저장된 데이터가 없을 경우, 크롤링한 데이터 Episode 테이블에 저장
            episode = Episode.objects.create(
                webtoon=Webtoon.objects.get(pk=pk),
                title=title,
                episode_id=episode_id,
                rating=rating,
                created_date=created_date)
            episode.save()
        # 데이터가 중복되는 경우, 데이터 저장하지 않음.
        else:
            print('이미 저장된 데이터입니다.')

    context = {
        'webtoon': webtoon

    }

    return render(request, 'webtoon/webtoon_detail.html', context)


def webtoon_add(request):
    # 웹툰 제목과, 웹툰 id 추가
    context = {}
    if request.method == 'POST':
        title = request.POST['title']
        webtoon_id = request.POST['webtoon_id']

        webtoon = Webtoon.objects.create(
            title=title,
            webtoon_id=webtoon_id)
        webtoon.save()

    return render(request, 'webtoon/webtoon_add.html', {})
