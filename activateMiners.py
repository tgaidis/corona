from streamMiner import wireTap
import tweepy
from tweepy import Stream

with open('/Users/theodore/Documents/GitHub/corona/access.txt', encoding= 'utf-8') as file:
    keys = file.readlines()
consumer_key = keys[0].strip('\n')
consumer_secret = keys[1].strip('\n')
access_token = keys[2].strip('\n')
access_token_secret = keys[3].strip('\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def main():
    
    covidStream = Stream(auth, wireTap('COVID.csv'))
    covidStream.filter(track = ['covid'])
    
    coronavirusStream = Stream(auth, wireTap('CORONAVIRUS.csv'))
    coronavirusStream.filter(track = ['coronavirus'])
    
    pandemicStream = Stream(auth, wireTap('PANDEMIC.csv'))
    pandemicStream.filter(track = ['pandemic'])
    
    


if __name__=="__main__":
    main()

