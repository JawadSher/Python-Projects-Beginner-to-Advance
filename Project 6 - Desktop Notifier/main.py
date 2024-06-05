import feedparser
from win10toast_click import ToastNotifier
import asyncio
import webbrowser


RSS_FEEDS = {
    "world": "http://rss.cnn.com/rss/edition_world.rss",
    "technology": "http://rss.cnn.com/rss/edition_technology.rss",
    "sports": "http://rss.cnn.com/rss/edition_sport.rss",
    "business": "http://rss.cnn.com/rss/money_news_international.rss",
    "health": "http://rss.cnn.com/rss/edition_health.rss",
    "science": "http://rss.cnn.com/rss/edition_space.rss",
    "entertainment": "http://rss.cnn.com/rss/edition_entertainment.rss"
}

string_length = 60
toaster = ToastNotifier()

def fetch_news(url):
    feed = feedparser.parse(url)
    return feed['entries']

def truncate_string(string, max_length):
    if len(string) > max_length:
        string[:max_length - 3] + "..."
    return string

def notify_news(news_item):
    title = truncate_string(news_item.get('title', 'No Title'), string_length)
    summary = truncate_string(news_item.get('summary', 'No Summary'), string_length)
    link = news_item.get('link', '')

    def openLink():
        webbrowser.open_new(link)

    toaster.show_toast(
        title=title,
        msg=summary,
        duration=10,
        icon_path=None,
        threaded=True,
        callback_on_click=openLink
    )

async def getUrl(url):
    seen_link = set()
    while True:
        news_items = fetch_news(url)
        for news_item in news_items:
            link = news_item.get('link', '')
            if link not in seen_link:
                seen_link.add(link)
                notify_news(news_item)
                await asyncio.sleep(10)
        await asyncio.sleep(10)

async def main():
    print("Please select category of the following Options : ")

    for category in RSS_FEEDS.keys():
        print(f'- {category}')
    
    selected_category = input("Enter the category : ").strip().lower()

    if selected_category not in RSS_FEEDS:
        print("Invalid Category !!!!")
        return
    
    url = RSS_FEEDS[selected_category]
    await getUrl(url)

if __name__ == '__main__':
    asyncio.run(main())

