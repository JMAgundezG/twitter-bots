from tweepy.streaming import StreamListener
from tweepy import Stream
import threading
import json
from twit_utilsBot import twit_utilsBot
import logging


#clase que escucha continuamente para nuevas interacciones
class PyStreamListener(StreamListener):

    def __init__(self,api):
        StreamListener.__init__(self)
        self.api = api

    #cada vez que se inserta una nueva interaccion no solo tweets
    def on_data(self, data):#trabajamos con el json
        tweet = json.loads(data)
        #print(tweet)



        try:
            #self.api.retweet(tweet['id']) esto retwitearía el tweet

            screen_name =tweet['user']['screen_name']
            utils =twit_utilsBot(self.api,screen_name)
            utils.listener(tweet)


        except Exception as ex:
           logging.error(ex)

        return True

    def on_error(self, status):
        print("ha habido un error con el tweet:",status.text);


#thread para poder ejecutar multiples cosas en un futuro
class StreamThread (threading.Thread):
    def __init__(self,api,auth):
        threading.Thread.__init__(self, group=None, target=None, name='streamThread')
        self.listener = PyStreamListener(api)
        self.stream = Stream(auth, self.listener)

    def run(self):
        self.stream.filter(track=['@JosemaBot'])#todo cambiar cuando se cambie la cuenta
