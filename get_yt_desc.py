import urllib.request
import re
import sys

def get_yt_desc(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # find meta description
        match = re.search(r'<meta name="description" content="(.*?)">', html)
        if match:
            print(f"Desc: {match.group(1)}")
        else:
            print("No meta description found")
    except Exception as e:
        print(f"Error: {e}")

get_yt_desc("uMOup3R0CdI")
