import tweepy
import sys
import os
from keys import keys, usr

consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_key = keys['access_key']
access_secret = keys['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

use = os.environ.get('TW_USERNAME')
class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
    	use = os.environ.get('TW_USERNAME')
    	try:
	    	if status.retweeted:
	    		return
	    	if status.user.screen_name.lower() == usr:
	    		return
	    	return api.retweet(id=status.id)
    	except:
        	return True

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
streamingAPI.filter(track=['#BellLetsTalk, #BellCause'])
