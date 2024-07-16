from __modules__.header_module import app_header
from __modules__.youtube_search_Module import media_search
from __modules__.youtube_Media_Downloader import downloadMedia 
import asyncio


async def media_search():
    media_search()

async def Download_Media():
    downloadMedia()

async def main():
    app_header()
    # await media_search()
    await downloadMedia()
    
if __name__ == '__main__':
    asyncio.run(main())