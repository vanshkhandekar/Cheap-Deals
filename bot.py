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

posted_hashes = set()

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": False
    }
    requests.post(url, data=payload)

def is_duplicate(text):
    h = hashlib.md5(text.encode("utf-8")).hexdigest()
    if h in posted_hashes:
        return True
    posted_hashes.add(h)
    return False

def format_message(source, title, link):
    message = (
        f"🔥 {source} DEAL ALERT\n\n"
        f"🛒 {title}\n\n"
        f"👉 Buy Now: {link}\n\n"
        f"📢 Join @everycheapdeals"
    )
    return message

def run_bot():
    for source, feed_url in RSS_FEEDS.items():
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            msg = format_message(source, entry.title, entry.link)
            if not is_duplicate(msg):
                send_message(CHANNEL_USERNAME, msg)
                time.sleep(3)

if __name__ == "__main__":
    send_message(ADMIN_USER_ID, "✅ GitHub Deals Bot Started")
    run_bot()🛒 {title}

👉 Buy Now: {link}

📢 Join @everycheapdeals
"""

def run_bot():
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            msg = format_msg(source, entry.title, entry.link)
            if not is_duplicate(msg):
                send_message(CHANNEL_USERNAME, msg)
                time.sleep(3)

if __name__ == "__main__":
    send_message(ADMIN_USER_ID, "✅ GitHub Deals Bot Started")
    run_bot()🛒 {title}

👉 Buy Now: {link}

📢 Join @everycheapdeals
"""

def run_bot():
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            msg = format_msg(source, entry.title, entry.link)
            if not is_duplicate(msg):
                send_message(CHANNEL_USERNAME, msg)
                time.sleep(3)

if __name__ == "__main__":
    send_message(ADMIN_USER_ID, "✅ GitHub Deals Bot Started")
    run_bot()🛒 {title}

👉 Buy Now: {link}

📢 Join @everycheapdeals
"""

def run_bot():
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            msg = format_msg(source, entry.title, entry.link)
            if not is_duplicate(msg):
                send_message(CHANNEL_USERNAME, msg)
                time.sleep(3)

if __name__ == "__main__":
    send_message(ADMIN_USER_ID, "✅ GitHub Deals Bot Started")
    run_bot()
