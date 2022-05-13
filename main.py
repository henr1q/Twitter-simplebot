import tweepy
from auth import create_api
import time

try:
    api = create_api()
except:
    print('API creation failed, verify your credentials in "auth.txt"')


# Reply/favorite/retweet with a query
def reply_to_query(query, lang, result_type, count, message, favorite=True, reply=True, retweet=True):
    tweets = api.search_tweets(q=query, lang=lang, result_type=result_type, count=count)
    for tweet in tweets:
        time.sleep(3)
        username = tweet.user.screen_name
        try:
            api.update_status(status=f'@{username} {message}', in_reply_to_status_id=tweet.id) if reply else 0
            tweet.favorite() if favorite else 0
            tweet.retweet() if retweet else 0
            print(f'replied: "{message}" to:@{username}')
        except tweepy.TweepyException as err:
            print(f"Couldn't work on this tweet: {err}")
    print('Done replying')


# Follow back who is following you
def follow_back():
    for follower in tweepy.Cursor(api.get_followers).items():
        follower.follow()
        print("Followed back everyone that is following you")


# Follow the followers of a specified user
def follow_followers(user):
    for follower in tweepy.Cursor(api.get_followers, screen_name=user).items():
        follower.follow()
        print(follower)
        print(f'followed:@{follower.screen_name}')


# query = the search query, result_type= recent, mixed, popular, count = number of tweets to query,
# message = reply quote
# if dont want to fav/rt/reply add favorite = False, etc
reply_to_query(query='query', lang='en', result_type='popular', count=10, message='message', favorite=False, retweet=False)
# follow_followers('user @')
# follow_back()