import feedparser
import yaml

FEED_URL = "https://medium.com/@sreekar.v22"
OUTFILE = "_data/medium.yml"

feed = feedparser.parse(FEED_URL)
posts = []
for entry in feed.entries[:5]:  # Fetch more than 3 in case you want
    posts.append({
        "title": entry.title,
        "url": entry.link,
        "date": entry.published,
        "summary": entry.summary
    })

with open(OUTFILE, "w") as f:
    yaml.dump({"posts": posts}, f, allow_unicode=True)
