from __modules__.header_module import app_header
from __modules__.youtube_search_Module import media_search 
import asyncio


async def main():
    app_header()
    await media_search()

if __name__ == '__main__':
    asyncio.run(main())