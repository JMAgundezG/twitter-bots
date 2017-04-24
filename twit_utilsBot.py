import time

class twit_utilsBot(object):
    def __init__(self):
        self.bot = Account()

    @staticmethod
    def count_word(list_of_words):
        aux = {}
        for i in list_of_words:
            if i in aux:
                aux[i]+=1
            else:
                aux[i] = 1

        a = sorted(aux.items(),key=lambda x:x[1],reverse=True)
        return a[0]


    def take_tweets_words(self,user):
        tweets = self.bot.user_timeline(user, count=1000)
        tweets_words = []
        for i in tweets:
            for j in i.text.split(" "):
                tweets_words.append(j)
        return tweets_words


    def listener(self, tweet):
        if "palabra_mas_usada" in tweet.text:
            a = count_word(take_tweets_words(tweet.user))
<<<<<<< HEAD
print(("la palabra más usada ha sido ",{1},", usada "{2}," veces").format(a[0],a[1]))
=======
            print(("la palabra más usada ha sido ",{1},", usada "{2}," veces").format(a[0],a[1]))
>>>>>>> 6f1e43597710d828a72a6d3f122ecbf26aee8a1d
