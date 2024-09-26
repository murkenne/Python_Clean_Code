'''
1. Refactoring a Weather Forecast Application into Classes and Modules
Objective: The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, 
object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes and organizing 
these classes into appropriate modules to enhance code readability, maintainability, and scalability.

Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. 
Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.
'''


class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, {})

class DataParser:
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:
    def __init__(self):
        self.weather_fetcher = WeatherDataFetcher()
        self.data_parser = DataParser()

    def display_weather(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.data_parser.parse_weather_data(data)
            print(weather_report)

    def get_detailed_forecast(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def run(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                self.display_weather(city)
