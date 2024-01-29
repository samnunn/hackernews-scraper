from bs4 import BeautifulSoup
import requests
import json
import datetime
import os

# gets data from https://news.ycombinator.com/front?day=YYYY_MM_DD
# returns 30 front page stories from that day ordered by _how much time they spent on the front page_

# settings
BASE_URL = os.environ.get('HN_FEED_BASEURL', 'https://example.com')
OUTPUT_PATH = os.environ.get('HN_FEED_BASEPATH', './')

# get yesterday's date
target_date = datetime.date.today() - datetime.timedelta(days=1)
formatted_date = target_date.strftime("%Y-%m-%d")

# get data from hn
hn_url = f'https://news.ycombinator.com/front?day={formatted_date}'
r = requests.get(hn_url)

# make soup
soup = BeautifulSoup(r.content, 'html.parser')

# get links
links_element_list = soup.css.select("tr.athing > td:last-of-type >span.titleline > a")
links_list = ""
for e in links_element_list:
    comments = "https://news.ycombinator.com/item?id=" + e.find_parent('tr')['id']
    title = e.string
    url = e.attrs.get('href')
    links_list += f"<li><a href='{url}'>{title}</a> (<a href='{comments}'>#</a>)</li>"

# make feed item
digest = {
    "id": hn_url,
    "url": hn_url,
    "title": f'Digest for {formatted_date}',
    "content_html": f'<ol>{links_list}</ol>',
    "date_published": target_date.isoformat(),
}

# make JSON feed
feed = {
	"version": "https://jsonfeed.org/version/1.1",
	"title": "Hacker News Digest",
	"favicon": f"{BASE_URL}/hackernews_icon.png",
	"icon": f"{BASE_URL}/hackernews_icon.png",
	"home_page_url": f"https://news.ycombinator.com/",
	"feed_url": f"{BASE_URL}/hackernews_yesterday.json",
	"items": [digest],
}

# save to disk
out = os.path.join(OUTPUT_PATH, 'hackernews-yesterday.json')
# with open(out, 'w') as f:
	# f.write(json.dumps(feed, indent=2))

print(json.dumps(feed, indent=2))