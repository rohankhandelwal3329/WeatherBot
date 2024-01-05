import tweepy
import requests
import time
from decouple import config

# Twitter API credentials
twitter_consumer_key = config('TWITTER_CONSUMER_KEY')
twitter_consumer_secret = config('TWITTER_CONSUMER_SECRET')
twitter_access_token = config('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET')
twitter_bearer_token = config('TWITTER_BEARER_TOKEN')

twitter_client = tweepy.Client(twitter_bearer_token, twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret)

# OpenWeatherMap API credentials
owm_api_key = config('OWM_API_KEY')

# List of top 5 cities
cities = ['London', 'New York', 'Tokyo', 'Paris', 'Beijing']

def fetch_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': city,
        'appid': owm_api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def weather_emoji(description):
    if description == 'clear sky':
        emoji = '🌞'
    elif description == 'few clouds':
        emoji = '⛅'
    elif description == 'overcast clouds':
        emoji = '☁️'
    elif description == 'scattered clouds':
        emoji = '☁️'
    elif description == 'broken clouds':
        emoji = '🌫️'
    elif description == 'shower rain':
        emoji = '🌦️'
    elif description == 'rain':
        emoji = '🌧️'
    elif description == 'thunderstorm':
        emoji = '⛈️'
    elif description == 'snow':
        emoji = '🌨️'
    elif description == 'mist':
        emoji = '🌫️'
    else:
        emoji = ''
    return emoji

def generate_combined_tweet_text(city_forecast_data):
    tweet_text = "🌦️ Weather forecast:\n"
    for city, forecast_data in city_forecast_data.items():
        temperature_min = forecast_data['list'][0]['main']['temp_min']
        temperature_max = forecast_data['list'][0]['main']['temp_max']
        description = forecast_data['list'][0]['weather'][0]['description']
        emoji_res = weather_emoji(description)
        tweet_text += f"{city}: ⬇️{temperature_min}°C ⬆️{temperature_max}°C, {description} {emoji_res}\n"

    tweet_text += "Have a good day❤️\n#WeatherBot #WeatherUpdate"
    return tweet_text

def post_weather_tweets():
    city_forecast_data = {}
    for city in cities:
        forecast_data = fetch_weather_data(city)
        city_forecast_data[city] = forecast_data
        time.sleep(5)  

    combined_tweet_text = generate_combined_tweet_text(city_forecast_data)
    twitter_client.create_tweet(text=combined_tweet_text)

    print('The weather forecast tweet has been posted successfully!!!')

if __name__ == "__main__":
    post_weather_tweets()
