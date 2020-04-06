"""Accesses Twitter data using Tweepy and collects information related to the COVID Epidemic"""
import tweepy
#Importing keys from textfile to provide security when uploading code to github
with open('access.txt', encoding= 'utf-8') as file:
    keys = file.readlines()

    consumer_key = keys[0].strip('\n')
    consumer_secret = keys[1].strip('\n')
    access_token = keys[2].strip('\n')
    access_token_secret = keys[3].strip('\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

query_1 = "COVID"
query_2 = "coronavirus"
query_3 = "pandemic"

language = "en"
query_1results = api.search(query_1, language)
query_2results = api.search(query_2, language)
query_3results = api.search(query_3, language)

for tweet in query_1results:
    print ("Username: ", tweet.user.screen_name, "Location: ", tweet.user.location)

for tweet in query_2results:
    print ("Username: ", tweet.user.screen_name, "Location: ", tweet.user.location)

for tweet in query_3results:
    print ("Username: ", tweet.user.screen_name, "Location: ", tweet.user.location)
