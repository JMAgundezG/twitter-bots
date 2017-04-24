import time
import tweepy
import logging

class twit_utilsBot(object):
    def __init__(self,api,screen_name):
        self.bot = api
        self.screen_name = screen_name

    @staticmethod
    def count_word(list_of_words):
        aux = {}
        for i in list_of_words:
            if i in aux:
                aux[i]+=1
            else:
                aux[i] = 1

        a = sorted(aux.items(),key=lambda x:x[1],reverse=True)
        for w in a :
            if len(w[0]) >4 and w[0] != 'RT':
                return w
        return a[0]


    def take_tweets_words(self,screen_name):


        tweets_words = []
        for i in tweepy.Cursor(self.bot.user_timeline,screen_name=screen_name).items(400):#devuelve los 200 ultimos tweets
            for j in i.text.split(" "):
                tweets_words.append(j)
        return tweets_words


    def listener(self, tweet):
        if "#cuentame" in tweet['text']:#si se está utilizando el hastag cuentame

            #obtenemos una tupla con la palbra mas usada y el número de veces de esta
            words = self.count_word(self.take_tweets_words(tweet['user']['screen_name']))
            #creamos el string del tweet aunque sea un poco lioso

            s = str('@'+tweet['user']['screen_name']+" tu palabra mas usada: "+ words[0]+"\nexactamente "+ str(words[1])+" veces")
            #twiteamos
            self.bot.update_status(s)
            print("Tu palabra mas usada ", words)


