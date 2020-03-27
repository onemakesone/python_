import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309'
data = requests.get(url, headers = headers)



soup = BeautifulSoup(data.text, 'html.parser')


musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 1
for genie in musics:
    a_tag = genie.select_one('td.info > a.title.ellipsis')
    title = a_tag.text
    if a_tag is not None:
        title = a_tag.text
        artist = genie.select_one('td.info > a.artist.ellipsis').text
        print(rank, ". ", title.strip(), "/", artist)
        rank += 1