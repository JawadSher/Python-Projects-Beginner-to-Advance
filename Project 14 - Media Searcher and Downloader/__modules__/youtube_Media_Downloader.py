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

