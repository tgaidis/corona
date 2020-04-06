"""Accesses Twitter data using Tweepy and collects information related to the COVID Epidemic"""
import tweepy
#Change to import from text file
consumer_key = "GKV6LnzsLYZX7kk60NSX4CKZ2"
consumer_secret = "541EdRFdcXxDUdVEopmzeJ0hnoUUjA13NMpWwv9EGPyzJaaUUv"
access_token = "1242151011470454787-nWOQKPk0DNENGMyEJ3YihcsdANgZuD"
access_token_secret = "QGH6RkM3YSE4leoXcZcAM1UYTgGV4ks3i4ItrWtSVV5Qw"

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