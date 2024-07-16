# Media Searcher and Downloader Project

This project is a Python-based application designed to search and download media from YouTube. It consists of several modules, each responsible for different functionalities, and offers a command-line interface for user interaction. The primary aim is to provide a streamlined way to search for media and download it with specific resolutions.

### Project Structure

-   `Application.py`: The main script that serves as the entry point of the application.
-   `__modules__/header_module.py`: Contains the function to display the application header.
-   `__modules__/youtube_search_Module.py`: Contains functions to search for YouTube videos.
-   `__modules__/youtube_Media_Downloader.py`: Contains functions to download YouTube videos.

### Functionality Overview

#### 1. Application Header (`__modules__/header_module.py`)

**Function: `app_header()`**

-   Displays a styled header for the application.
-   Uses a loop to print the header text character by character with delays for a typewriter effect.



```
import sys
import time

def app_header():
    input_str = '''===========================================\n\tMedia Search and Downloader\n==========================================='''
    sys.stdout.write('\n')
    for c in input_str:
        if c == '=':
            time.sleep(0.01)
        else:
            time.sleep(0.1)

        sys.stdout.write(c)
        sys.stdout.flush() 
    sys.stdout.write('\n')
   ``` 

#### 2. Media Search Module (`__modules__/youtube_search_Module.py`)

**Functions:**

-   `search_query(user_query, r_limit)`: Uses the `pytube` library to search for YouTube videos based on user input.
-   `media_search()`: Asks the user for a search term and result limit, then displays the search results with video titles, URLs, and thumbnails.


```
from pytube import Search
from pytube import YouTube
import asyncio

async def search_query(user_query, r_limit):
    q = Search(user_query)
    results = []

    while len(results) < r_limit:
        next_results = q.results
        if not next_results:
            break
        results.extend(next_results)

    search_term = user_query
    video_info = [{'title': video.title, 'video_id': video.video_id, 'thumbnail': video.thumbnail_url} for video in results]

    return search_term, video_info[:r_limit]

async def media_search():
    try:
        user_input = input("Search here : ")
        result_limit = int(input("Set Result Limit : "))
        query_results = await search_query(user_input, result_limit)

        search_term, video_info = query_results
        print()
        print('-------------------------------------- Result ---------------------------------------')
        print(f'Search Term : {search_term}')
        print()

        for num, video_info in enumerate(video_info, start=1):
            print(f'{num} | Title  ==> {video_info["title"]} <==\n   | URL : https://www.youtube.com/watch?v={video_info["video_id"]}\n   | Thumbnail : {video_info["thumbnail"]}\n-------------------------------------------------------------------------------\n')
    except Exception as e:
        print(f"Error occurred : {e}")
``` 

#### 3. Media Downloader Module (`__modules__/youtube_Media_Downloader.py`)

**Functions:**

-   `get_default_dir()`: Returns the default directory for downloads.
-   `download_media(url, save_to, resolution)`: Downloads a YouTube video at the specified resolution using `yt_dlp` and saves it to the specified directory.
-   `downloadMedia()`: Prompts the user for the video URL, save directory, and desired resolution, then calls `download_media`.



```
import yt_dlp
import os
import argparse
from win10toast import ToastNotifier

def get_default_dir():
    return os.path.join(os.path.expanduser('~'), "Downloads")

def download_media(url, save_to=None, resolution=None):
    if not save_to:
        save_to = get_default_dir()

    if not os.path.exists(save_to):
        os.mkdir(save_to, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(save_to, '%(title)s.%(ext)s'),  # Output path and filename template
        'format': 'bestvideo[height<=?{0}]+bestaudio/best[height<=?{0}]'.format(resolution or '1080')
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            downloaded_file_path = os.path.join(save_to, f"{info_dict.get('title')}.mp4")
            ToastNotifier().show_toast('Downloading Completed Successfully', f'File saved to : {downloaded_file_path}')
            print(f"Download completed successfully. File saved to: {downloaded_file_path}")

            print('\n------------------------------Video Info------------------------------\n')
            print(f"Title: {info_dict.get('title')}")
            print(f"Author: {info_dict.get('uploader')}")
            print(f"Views: {info_dict.get('view_count')}")
            print(f"Length: {info_dict.get('duration')} seconds")
            print(f"Description: {info_dict.get('description')}")
            print('------------------------------------------------------------------------\n')

    except Exception as e:
        print(f"An error occurred: {e}")

def downloadMedia():
    url = input("Enter URL Here: ")
    save_to = input("Save to (default is 'Downloads'): ").strip()
    resolution = input("Enter desired resolution (e.g., 360p, 720p): ").strip()
    download_media(url, save_to, resolution)
   ``` 

#### 4. Main Application (`Application.py`)

**Functionality:**

-   Displays the application header.
-   Provides a command-line interface with options to search for media, download media, or exit the application.
-   Uses async functions to handle media search and download operations efficiently.

```
from __modules__.header_module import app_header
from __modules__.youtube_search_Module import media_search as search_media
from __modules__.youtube_Media_Downloader import downloadMedia

async def search_media_function():
    await search_media()

def download_media_function():
    downloadMedia()

async def main():
    app_header()

    while True:
        print("1. Search Social Media")
        print("2. Download Media")
        print("3. Exit")
        print()

        select_option = input("Select Option: ")

        if select_option == '1':
            while True:
                await search_media_function()
                user_choice = input('Type "exit" to Main Menu: ')
                if user_choice.lower() == 'exit':
                    break
        
        elif select_option == '2':
            while True:
                download_media_function()
                user_choice = input('Type "exit" to Main Menu: ')
                if user_choice.lower() == 'exit':
                    break
        
        elif select_option == '3':
            break
        
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
   ``` 

### Usage

1.  **Search Social Media**:
    
    -   Select option 1.
    -   Enter a search term and the number of results to display.
    -   View the search results with video titles, URLs, and thumbnails.
2.  **Download Media**:
    
    -   Select option 2.
    -   Enter the URL of the video, the directory to save the video (default is Downloads), and the desired resolution.
    -   The video will be downloaded, and a notification will be displayed upon completion.
3.  **Exit**:
    
    -   Select option 3 to exit the application.

### Dependencies

-   `pytube`
-   `yt_dlp`
-   `win10toast`
-   `asyncio`

### Installation

1.  Clone the repository:
    

    
    ```
    git clone https://github.com/JawadSher/Python-Projects-Beginner-to-Advance/tree/main/Project%2014%20-%20Media%20Searcher%20and%20Downloader
    cd Media-Searcher-and-Downloader
    ``` 
    
2.  Install the required dependencies:
    

    
    ```
    pip install pytube yt-dlp win10toast
    ``` 
    
3.  Run the application:
    
    
    ```
    python Application.py
    ``` 
    

### Conclusion

This project provides a comprehensive tool for searching and downloading media from YouTube, with a user-friendly command-line interface and clear separation of functionalities across different modules. The use of async functions ensures efficient handling of I/O-bound operations, making the application responsive and efficient.
