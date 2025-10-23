import time
import feedparser
from win10toast import ToastNotifier
import os

# Create notifier
toaster = ToastNotifier()

# RSS feed (you can change this to another source, e.g. Google News, CNN, etc.)
RSS_URL = "http://feeds.bbci.co.uk/news/rss.xml"

# Path to icon (optional)
ICON_PATH = r"C:\Users\jakka\OneDrive\Desktop\icons\VS_CODE.png.jpeg"
if not os.path.exists(ICON_PATH):
    ICON_PATH = None  # fallback if icon not found

# Parse the RSS feed
feed = feedparser.parse(RSS_URL)

# Show the top 3 news items
for entry in feed.entries[:3]:
    title = entry.title
    description = entry.get("summary", "No description available.")
    
    toaster.show_toast(
        title,
        description,
        icon_path=ICON_PATH,
        duration=30
    )
    time.sleep(15)  # delay between notifications

print("News notifications shown successfully!")
