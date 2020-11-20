import requests
import tweepy
import os

from dotenv import load_dotenv
load_dotenv()

def get_joke():
      endpoint = 'http://api.icndb.com/jokes/random'

      response = requests.get(endpoint)
      response.raise_for_status()
      joke = response.json()
      return joke['value']['joke']

def oAuth():
      api_key = os.environ['TWITTER_API_KEY']
      secret_key = os.environ['TWITTER_SECRET_KEY']
      access_token = os.environ['TWITTER_ACCESS_TOKEN']
      access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

      #authenticating to access the twitter API
      auth=tweepy.OAuthHandler(api_key, secret_key)
      auth.set_access_token(access_token,access_token_secret)
      #api=tweepy.API(auth)

      return auth

def tweet_joke():
      o_Auth = oAuth()
      api = tweepy.API(o_Auth)

      try:
            joke = get_joke()
            post_tweet = api.update_status(f'Chuck Norris Joke Bot says: {joke}')
            return post_tweet
      except Exception as e:
            print(e)
      


if __name__ == '__main__':
    tweet_joke()

    
