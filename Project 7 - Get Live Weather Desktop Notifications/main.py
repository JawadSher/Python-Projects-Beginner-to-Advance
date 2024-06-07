import aiohttp
import asyncio
import logging
import argparse
from win10toast import ToastNotifier

logging.basicConfig(level=logging.INFO)
notifier = ToastNotifier()

async def fetch_data(url):
    API_KEY = "apikey=0zN2ZgXItrVsy4GfQQlz6HEcgMY55t8U"
    headers = {"accept": "application/json"}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url + API_KEY, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            logging.error(f'Failed to fetch data {e}')
            return

async def formate_data(data):
    if "timelines" in data and 'minutely' in data['timelines']:
        first_entry = data['timelines']['minutely'][0]
        time = first_entry['time']
        values = first_entry['values']

        data_Summary = (
            f"Time: {time}\n"
            f"Temperature: {values['temperature']} °C\n"
            f"Apparent Temperature: {values['temperatureApparent']} °C\n"
            f"Humidity: {values['humidity']} %\n"
            f"Precipitation Probability: {values['precipitationProbability']} %\n"
            f"Rain Intensity: {values['rainIntensity']} mm/hr\n"
            f"Wind Speed: {values['windSpeed']} m/s\n"
            f"Wind Direction: {values['windDirection']}°\n"
            f"Visibility: {values['visibility']} km\n"
            f"Cloud Cover: {values['cloudCover']} %\n"
        )
        
        return data_Summary
    else:
        return 'No weather data available at this movement.'

async def main(location, update_interval, notification_duration):
    while True:
        URL = f'https://api.tomorrow.io/v4/weather/forecast?location={location}&'
        weather_data = await fetch_data(URL)
        if weather_data:
            weather_Summary = await formate_data(weather_data)
            logging.info(f'Weather data fetched {weather_Summary}')
            notifier.show_toast(f'Live Weather Update {location}', weather_Summary, duration=notification_duration)
        else:
            logging.error("failed to fetch weather data")
        
        logging.info(f'Waiting for {update_interval} seconds before next update.')
        await asyncio.sleep(update_interval)

if __name__ == '__main__':
    parser =  argparse.ArgumentParser(description="Live Weather Notification")
    parser.add_argument('location', help='Location for weather (e.g. Pakistan, PK)')
    parser.add_argument('-u', '--update-interval', type=int, default=3600, help="Update interval in seconds (Default : 3600)")
    parser.add_argument('-d', '--notification-duration', type=int, default=3, help="Duration of Notification in seconds (Default : 3)")

    args = parser.parse_args()

    asyncio.run(main(args.location, args.update_interval, args.notification_duration))