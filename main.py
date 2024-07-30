import requests  # Import the requests module to make HTTP requests
from datetime import datetime  # Import datetime to handle date and time conversion

# Fetch and display weather information for a given city.
def get_weather():
    # Prompt the user to enter the city name
    city = input("Enter city name: ")
    
    # Define the API key and URL for the OpenWeatherMap API
    api_key = "f68c6225c16d37037694680f47ff74e5" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Make a GET request to the API URL
    response = requests.get(url)
    # Parse the JSON response data
    data = response.json()

    # Check if the response contains an error code
    if data.get("cod") != 200:
        print("Error fetching data.")
        return

    # Extract relevant information from the response data
    city = data["name"].capitalize()  # Capitalize the city name
    description = data["weather"][0]["description"]  # Get weather description
    temperature = data["main"]["temp"]  # Get temperature in Celsius
    pressure = data["main"]["pressure"]  # Get atmospheric pressure in hPa
    humidity = data["main"]["humidity"]  # Get humidity percentage
    wind = data["wind"]["speed"]  # Get wind speed in km/h
    sunrise = data["sys"]["sunrise"]  # Get sunrise time in Unix timestamp
    sunset = data["sys"]["sunset"]  # Get sunset time in Unix timestamp
    
    # Display the weather information
    print(f"\nWeather in {city}:")
    print(f"Description: {description.capitalize()}")
    print(f"Temperature: {temperature}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind} km/h")
    print(f"Sunrise: {datetime.fromtimestamp(sunrise).strftime('%I %p').lstrip('0')}")
    print(f"Sunset: {datetime.fromtimestamp(sunset).strftime('%I %p').lstrip('0')}")

# Call the get_weather function to run the program
get_weather()
