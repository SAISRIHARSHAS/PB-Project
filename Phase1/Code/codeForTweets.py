from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time 
import json


ckey="ycCB7onSCfcA1e9K0ZUzVY2GA"
csecret="bzZBxbycwIqyB97UOA5llVZcG7OFczlwVU0Bvmvp1tUOoGw93W"
atoken="768298204567711744-8REnbwuK8dPT8LLRMm2hlMFbesnWbWK"
asecret="uX4si9CirS4pp8OhFME3ZaIwyfvT7bPyFcZh0KRyCWjZX"

class listener(StreamListener):
    def on_data(self, data):

        try:
            tweet_data = json.loads(data)
            tweet = tweet_data["text"]
            writeTweets = open('tweet_p1.json','a')
            writeTweets.write(tweet)
            writeTweets.close()
            return(True)

        except Exception as e:
            time.sleep(1)

        def on_error(self, status):
            print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#MissAmerica,#Patriots,#WWEBacklash"])
