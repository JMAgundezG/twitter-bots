from tweepy.streaming import StreamListener
from tweepy import Stream
import threading
import json



class PyStreamListener(StreamListener):

    def __init__(self,api):
        StreamListener.__init__(self)
        self.api = api

    def on_data(self, data):
        tweet = json.loads(data)
        try:
             self.api.retweet(tweet['id'])

        except Exception as ex:
           print ( "error")

        return True

    def on_error(self, status):
        print("ha habido un error con el tweet:",status.text);


class StreamThread (threading.Thread):
    def __init__(self,api,auth):
        threading.Thread.__init__(self, group=None, target=None, name='streamThread')
        self.listener = PyStreamListener(api)
        self.stream = Stream(auth, self.listener)

    def run(self):
        self.stream.filter(track=['@Josemabot'])
