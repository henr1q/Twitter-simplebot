import tweepy
import configparser

config = configparser.ConfigParser()
config.read('auth.txt')
api_key = config.get('apikey', 'key')
api_secret = config.get('apikey', 'key_secret')
access_token = config.get('apikey', 'access_token')
access_token_secret = config.get('apikey', 'access_token_secret')


def create_api():
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    if api.verify_credentials():
        print("Api created")
        return api
    else:
        print("Api auth failed, verify your access")


