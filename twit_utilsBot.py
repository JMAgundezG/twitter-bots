import time
import tweepy
import logging
import db_methods

class twit_utilsBot(object):
    def __init__(self,api,screen_name):
        self.bot = api
        self.screen_name = screen_name

    """devuelve la palabra más usada de la lista de palabras siempre
    y cuando cumpla unas reglas determinadas"""
    @staticmethod
    def count_word(list_of_words):
        aux = {} #diccionario para almacenar
        for i in list_of_words:
            if i in aux:
                aux[i]+=1
            else:
                aux[i] = 1

        a = sorted(aux.items(),key=lambda x:x[1],reverse=True)#se ordenan por value del diccionario

        for w in a :
            #si tiene un tamaño mayor a 3, no es RT y no es una mención
            if len(w[0]) >3 and w[0] != 'RT' and '@' not in w[0]:
                return w
        return a[0]

    """devuelve la persona mas veces mencionada como un dicionario key value"""
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

    """obtiene en una lista las palabras más usadas de los últimos 400 tweets"""
    def take_tweets_words(self,screen_name):
        tweets_words = []
        #obtenemos los ultimos 400 tweets de una persona el nombre se especifica en el screname
        for tweet in tweepy.Cursor(self.bot.user_timeline,screen_name=screen_name).items(400):
            for j in tweet.split(" "):
                tweets_words.append(j)
        return tweets_words

    def tieneInsulto(self,s):
        ins = db_methods.listaInsultos()
        sl = s.lower()
        # devuelve true si en cualquiera de los elementos del tweet está en el insulto

        return any(map(lambda x: x.lower() in sl.split(), ins))


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


        elif self.tieneInsulto(tweet['text']):
            s = '@{} oye un respeto tú >:@'.format(tweet['user']['screen_name'])
            self.bot.update_status(s)




