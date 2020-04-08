"""Accesses Twitter data using Tweepy and collects information related to the COVID Epidemic"""
import tweepy

def tweetMiner(codes, query, language = 'en', tweet_type = 'recent'):
    with open(codes, encoding= 'utf-8') as file:
        keys = file.readlines()
    consumer_key = keys[0].strip('\n')
    consumer_secret = keys[1].strip('\n')
    access_token = keys[2].strip('\n')
    access_token_secret = keys[3].strip('\n')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #results = api.search(query, language, tweet_type)
    ##temp = 0
    """
    for tweet in results:
        print(tweet.id)
        print(temp)
        temp += 1
    """
