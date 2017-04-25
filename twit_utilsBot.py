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
            #si tiene un tamaño mayor a 3, no es RT y no es una mención
            if len(w[0]) >3 and w[0] != 'RT' and '@' not in w[0]:
                return w
        return a[0]

    """devuelve la persona mas veces mencionada como un diccionario"""
    @staticmethod
    def count_mention(list_of_words):
        aux = {}
        for i in list_of_words:
            if i in aux:
                aux[i]+=1
            elif '@' in i:
                aux[i] = 1

        a = sorted(aux.items(),key=lambda x:x[1],reverse=True)
        return a[0]


    def take_tweets_words(self,screen_name):
        tweets_words = []
        #obtenemos los ultimos 400 tweets de una persona
        for i in tweepy.Cursor(self.bot.user_timeline,screen_name=screen_name).items(400):
            for j in i.text.split(" "):
                tweets_words.append(j)
        return tweets_words


    def listener(self, tweet):

        if "#cuentame" in tweet['text']:#si se está utilizando el hastag cuentame

            #obtenemos una tupla con la palbra mas usada y el número de veces de esta
            word_list = self.take_tweets_words(tweet['user']['screen_name'])
            word = self.count_word(word_list)

            #creamos el string del tweet aunque sea un poco lioso
            s = str('@'+tweet['user']['screen_name']+" tu palabra mas usada: "+ word[0]+"\nexactamente "+ str(word[1])+" veces")
            #twiteamos
            self.bot.update_status(s)
            print("Tu palabra mas usada ", word)

        elif "#miCrush" in tweet['text']:
            word_list = self.take_tweets_words(tweet['user']['screen_name'])
            word = self.count_mention(word_list)
            # creamos el string del tweet aunque sea un poco lioso
            s = str('@' + tweet['user']['screen_name'] + " mayor mención: " + word[0] + "\ntotal " + str(
                word[1]) + " veces")
            self.bot.update_status(s)
            print('@' + tweet['user']['screen_name'] + " mayor mención: " + word[0] + "\ntotal " + str(
                word[1]) + " veces")
        elif "imbécil" in tweet['text'] or "gilipollas" in tweet['text']:
            s = '@{} tu puta madre hijo de puta >:@'.format(tweet['user']['screen_name'])
            self.bot.update_status(s)
