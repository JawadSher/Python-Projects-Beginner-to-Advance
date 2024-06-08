<h1 align='center'>Get Live Weather Desktop Notifications Project</h1>

## Source Code Explanation
  ### **Imports:**
  -   `import aiohttp`: Enables making asynchronous HTTP requests using the `aiohttp` library.
  -   `import asyncio`: Provides functionalities for asynchronous programming.
  -   `import logging`: Facilitates logging messages for debugging and monitoring purposes.
  -   `import argparse`: Allows for parsing command-line arguments when running the script.
  -   `from win10toast import ToastNotifier`: Imports the `ToastNotifier` class from the `win10toast` library for displaying toast notifications (Windows-specific).
  
  ### **Logging Configuration:**
  
  -   `logging.basicConfig(level=logging.INFO)`: Sets up the basic logging configuration to print messages with a severity level of `INFO` (and higher) to the console.
  
  ### **Toast Notifier Initialization:**
  
  -   `notifier = ToastNotifier()`: Creates an instance of the `ToastNotifier` class, which will be used to display toast notifications.
  
  ### **`fetch_data` Function:**
  
  -   `async def fetch_data(url):`: Defines an asynchronous function named `fetch_data` that takes a URL as input.
  -   `API_KEY = "apikey=YOUR_API_KEY"`: Stores your Tomorrow.io API key (replace `YOUR_API_KEY` with your actual key). This key is crucial for accessing weather data from the Tomorrow.io API.
      -   **Important:** Never store your API key directly in the code. Consider environment variables or a configuration file for a more secure approach.
        
  -   `headers = {"accept": "application/json"}`: Sets the HTTP header to specify that the function expects JSON data in response.
  -   `async with aiohttp.ClientSession() as session:`: Establishes an asynchronous context manager using `aiohttp.ClientSession()`. This context manager will handle creating and closing the HTTP session efficiently.
      -   **Note:**  `aiohttp.ClientSession()` is specifically designed for asynchronous HTTP requests.
        
  -   `try:`: Initiates a `try` block to handle potential exceptions during the HTTP request.
      -   `async with session.get(url + API_KEY, headers=headers) as response:`: Makes an asynchronous GET request using the `session` object. It appends the API key to the URL and sets the specified headers.
          -   `response.raise_for_status()`: Raises an exception if the response status code indicates an error.
      -   `return await response.json()`: Awaits the asynchronous response and returns the parsed JSON data (if successful).
        
  -   `except aiohttp.ClientError as e:`: Catches exceptions of type `aiohttp.ClientError` that might occur during the HTTP request.
      -   `logging.error(f'Failed to fetch data {e}')`: Logs an error message with details about the exception.
      -   `return`: Returns `None` to indicate that no data could be fetched.
  
  ### **`formate_data` Function:**
  
  -   `async def formate_data(data):`: Defines an asynchronous function named `formate_data` that takes weather data as input (assumed to be in JSON format).
  -   `if "timelines" in data and 'minutely' in data['timelines']:`: Checks if the JSON data has the expected structure, containing "timelines" and "minutely" keys.
      -   `first_entry = data['timelines']['minutely'][0]`: Extracts the first entry (representing the current weather) from the "minutely" timeline.
      -   `time = first_entry['time']`: Retrieves the time from the entry.
      -   `values = first_entry['values']`: Extracts the weather values from the entry.
        
  -   `data_Summary = ...`: Constructs a multi-line string containing formatted weather data using f-strings.
  -   `else:`: If the expected structure is not found, the message "No weather data available at this movement." is returned.
  -   `return data_Summary`: Returns the formatted weather summary or the "No data" message.

  ### **`main` Function:**
  
  -   `async def main(location, update_interval, notification_duration):`: Defines an asynchronous function named `main` that takes three arguments:
      -   `location`: The location for which to fetch weather data (e.g., "Pakistan, PK").
      -   `update_interval`: The interval between weather updates in seconds (default: 36
   
  ## Usage of weather_notifier.py

This Python script provides live weather notifications on your Windows system using the Tomorrow.io API. Here's how to use it:

### **Requirements:**

  -   Python 3.x
  -   `aiohttp` library: Install with `pip install aiohttp`
  -   `win10toast` library (Windows-specific): Install with `pip install win10toast`
  -   A Tomorrow.io API key: Create a free account at [https://app.tomorrow.io/signup](https://app.tomorrow.io/signup) and obtain an API key.
  
  **Instructions:**
  
  1.  **Obtain Your API Key:**
      
      -   Sign up for a free Tomorrow.io account ([https://app.tomorrow.io/signup](https://app.tomorrow.io/signup)).
      -   Go to your account settings and navigate to the API section.
      -   Generate a new API key or use an existing one.
  2.  **Replace the Placeholder API Key:**
      
      -   Open the `weather_notifier.py` script in a text editor.
      -   Find the line `API_KEY = "apikey=YOUR_API_KEY"` and replace `YOUR_API_KEY` with your actual API key.
      -   **Important:** Never store your API key directly in the code. Consider using environment variables or a separate configuration file for better security.
  3.  **Run the Script:**
      
      -   Open a terminal or command prompt and navigate to the directory where you saved the script.
      -   Run the script with the following command, replacing `LOCATION` with your desired location code (e.g.,  `Pakistan, PK`):

        **Bash**
         ```
         python weather_notifier.py LOCATION
         ```
         
  4. **Optional Arguments:**
     
     - ```-u```,  ```--update-interval``` : Specify the update interval in seconds between weather checks (default: 3600 seconds, or 1 hour).
    
     -  ```-d```,  ```--notification-duration``` : Set the duration for which the toast notification should stay visible in seconds (default: 3 seconds).
    
      ```
      python weather_notifier.py LOCATION -u 1800 -d 5  # Update every 30 minutes (1800 seconds) with a 5-second notification duration
      ```
    
