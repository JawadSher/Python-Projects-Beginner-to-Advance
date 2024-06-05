# Desktop Notifier - News Notifier

This Python script fetches news articles from various categories such as world, technology, sports, business, health, science, and entertainment from CNN's RSS feeds and displays toast notifications on Windows 10. Users can click on the notifications to open the corresponding news articles in their web browser.

## How it Works

1. **RSS Feeds Configuration**: The script is configured with RSS feed URLs for different news categories from CNN.

2. **Notification Setup**: It uses the `win10toast-click` library to create toast notifications on Windows 10. Notifications include the title and summary of news articles truncated to a maximum length.

3. **Fetching News**: The script fetches news articles from the provided RSS feed URL using the `feedparser` library.

4. **Truncating Strings**: A helper function is used to truncate long strings (title and summary) to a specified maximum length to fit within the notification window.

5. **Showing Notifications**: The `notify_news` function creates and displays toast notifications for each news article fetched. Clicking on a notification opens the corresponding news article in the default web browser.

6. **Main Loop**: An asynchronous main loop periodically fetches news articles from the selected category's RSS feed and displays notifications for new articles.

7. **User Interaction**: Users are prompted to select a news category from the available options. If an invalid category is selected, an error message is displayed.

## Usage

1. Clone the repository.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Run the script using `python news_notifier.py`.
4. Follow the on-screen instructions to select a news category.

## Requirements

- Python 3.x
- `feedparser` library
- `win10toast-click` library

## Example

```bash
$ python news_notifier.py
Please select a news category from the following options:
- world
- technology
- sports
- business
- health
- science
- entertainment
Enter the category: health
