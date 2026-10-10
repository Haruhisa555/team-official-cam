import urllib.request
import re
import sys

def search(query):
    query = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={query}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        video_ids = re.findall(r"watch\?v=(\S{11})", html)
        if video_ids:
            return video_ids[0]
    except Exception as e:
        print(f"Error: {e}")
    return None

id1 = search("涙の初陣 日本ウェルネススポーツ大学女子駅伝部が創部２年目で初めて大学駅伝に出場 team official cam")
id2 = search("今年ダメなら監督辞めることになるとおもいます コモディイイダ team official cam")

print(f"Video 1 ID: {id1}")
print(f"Video 2 ID: {id2}")
