"""Mines Twitter Data Stream in real time"""
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import time

class wireTap(StreamListener):
    """Creates an instance of a twitter stream grabber that grabs all tweets using a specific keyword"""
    def on_data(self, data):
    """Opens the twitter data stream, limits data down to desired attributes, and appends the data to a CSV
        Info includes dat/time, and tweet ID)
        Args:
            data: String of data from each tweet:
        Returns:
            True: Returns true if completed successfully
        Side Effects:
            Appends desired information from each new tweet into a locally stored CSV File
    """
        try:
        #print(type(data))
            tweetDate = data.split('"created_at":"')[1].split('","id"')[0]
            saveData = open('storeTweets.csv', 'a')
            saveData.write(tweetDate)
            saveData.write('\n')
            saveData.close()
            #print(tweetDate)
            return True
        
        except BaseException:
            print('failed ondata')
            time.sleep(10)
        return True

    def on_error(self, status):
    """Checks the status of the data stream.  
        Args:
            status - status of the data stream
        returns:
            False if there is an error
    """
        print (status)
        if status == 420:
            print('error')
            return False

with open('access.txt', encoding= 'utf-8') as file:
    keys = file.readlines()
consumer_key = keys[0].strip('\n')
consumer_secret = keys[1].strip('\n')
access_token = keys[2].strip('\n')
access_token_secret = keys[3].strip('\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

covidStream = Stream(auth, wireTap())
covidStream.filter(track = ['covid'])

coronavirusStream = Stream(auth, wireTap())
coronavirusStream.filter(track = ['coronavirus'])



