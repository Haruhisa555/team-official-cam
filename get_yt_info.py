import urllib.request
import re
import sys

def get_yt_info(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        title_match = re.search(r'<title>(.*?)</title>', html)
        title = title_match.group(1) if title_match else "No title"
        title = title.replace(" - YouTube", "")
        print(f"Title: {title}")
    except Exception as e:
        print(f"Error: {e}")

get_yt_info("uMOup3R0CdI")
