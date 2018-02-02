import os

import re
import requests
from bs4 import BeautifulSoup

PATH_MODULE = os.path.abspath(__file__)
print(PATH_MODULE)
ROOT_DIR = os.path.dirname(PATH_MODULE)
print(ROOT_DIR)


class EpisodeData:
    """
    하나의 에피소드에 대한 정보를 갖도록 함
    """

    def __init__(self, episode_id, url_thumbnail, title, rating, created_date):
        self.episode_id = episode_id
        self.url_thumbnail = url_thumbnail
        self.title = title
        self.rating = rating
        self.created_date = created_date


def get_episode_list(webtoon_id, page, refresh_html=None):
    """
        고유ID(URL에서 titleId값)에 해당하는 웹툰의
        특정 page에 있는 에피소드 목록을 리스트로 리턴
        1. html 파일 저장
        2. 읽어오기
        3. 크롤링 (페이지마다 어떻게 할것인가에 대해서생각)
        4. 리턴하지 말고 자신의 데이터 속성들을 EpisodeData 속성으로 할당
    """

    # 파일 입력
    file_name = f'webtoon_data_{webtoon_id}.html'
    file_path = os.path.join(ROOT_DIR, file_name)

    try:
        file_mode = 'wt' if not os.path.exists(file_path) else 'xt'
        with open(file_path, file_mode) as f:
            url = "http://comic.naver.com/webtoon/list.nhn"
            params = {
                'titleId': webtoon_id,
                'page': page
            }
            response = requests.get(url, params)
            # # page 확인
            # print(response.url)
            source = response.text
            f.write(source)
    except FileExistsError:
        print(f'"{file_path}" file is already exists!')

    source = open(file_path, 'rt').read()
    soup = BeautifulSoup(source, 'lxml')

    tbody = soup.select('table.viewList > tr')
    result = list()
    for td in tbody:
        number = td.find('a').get('onclick')
        episode_id = re.search(r".*(\d+)?,'(\d+)'",number).group(2)
        img = td.find('img').get('src')
        title = td.find('td',class_="title").get_text(strip =True)
        rating = td.select_one('div.rating_type > strong').text
        created_date =td.find('td',class_="num").get_text(strip =True)

        episode = EpisodeData(episode_id,img,title,rating,created_date)
        result.append({
            'episode_id':episode_id,
            'img':img,
            'title':title,
            'rating':rating,
            'created_date':created_date
        })

    return result


if __name__ == '__main__':
    webtoon =  get_episode_list(703835, 1)
    for episode in webtoon:
        print(episode)