# WeatherBot

WeatherBot is a Python script that posts weather forecast updates for multiple cities on Twitter using the Twitter API and OpenWeatherMap API.

# Features:

- Fetches weather data for predefined cities.
- Generates a weather forecast tweet with temperature, weather description, and emojis.
- Posts the combined weather forecast tweet on Twitter.

# Requirements:

- Python 3.x
- Tweepy library
- Requests library
- Decouple library
- OpenWeatherMap API key
- Twitter API credentials

# 1. Clone the repository
   git clone https://github.com/rohankhandelwal3329/WeatherBot.git
   cd WeatherBot

# 2. Create a .env file in the project root and add your API keys:
   TWITTER_CONSUMER_KEY= your_twitter_consumer_key
   TWITTER_CONSUMER_SECRET= your_twitter_consumer_secret
   TWITTER_ACCESS_TOKEN= your_twitter_access_token
   TWITTER_ACCESS_TOKEN_SECRET= your_twitter_access_token_secret
   TWITTER_BEARER_TOKEN= your_twitter_bearer_token
   OWM_API_KEY= your_openweathermap_api_key

# 3. Run the script
   python weather_bot.py


