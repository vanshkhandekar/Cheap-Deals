import feedparser
import requests
import hashlib
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")

RSS_FEEDS = {
    "Amazon": "https://www.amazon.in/gp/rss/bestsellers",
    "Flipkart": "https://www.flipkart.com/rss",
    "Meesho": "https://www.meesho.com/rss"
}

posted = set()

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": False
    }
    requests.post(url, data=data)

def is_duplicate(text):
    h = hashlib.md5(text.encode("utf-8")).hexdigest()
    if h in posted:
        return True
    posted.add(h)
    return False

def build_message(source, title, link):
    return (
        f"{source} DEAL ALERT\n\n"
        f"Product: {title}\n\n"
        f"Buy Now: {link}\n\n"
        f"Join @everycheapdeals"
    )

def run_bot():
    for source, feed_url in RSS_FEEDS.items():
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            msg = build_message(source, entry.title, entry.link)
            if not is_duplicate(msg):
                send_message(CHANNEL_USERNAME, msg)
                time.sleep(3)

if __name__ == "__main__":
    send_message(ADMIN_USER_ID, "GitHub Deals Bot Started")
    run_bot()
