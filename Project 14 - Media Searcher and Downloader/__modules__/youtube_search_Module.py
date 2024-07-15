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
            print(f'{num} | Title  ==> {video_info['title']} <==\n   | URL : https://www.youtube.com/watch?v={video_info['video_id']}\n   | Thumbnail : {video_info['thumbnail']}\n-------------------------------------------------------------------------------\n')
    except Exception as e:
        print(f"Error occurred : {e}")

