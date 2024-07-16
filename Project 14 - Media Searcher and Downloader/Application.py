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
