#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys , json,stream


argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'g9jV0AvYulcZiwO0YoJVT1avo'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'F9Y6QD7ig9XMZZt4cwou1w5EjRG29gFDpymsFphKrWV8bNsjpF'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '856150797607895041-d9MCdKVh6XOxemBjtKr7VHJI1YkfaIX'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'eq6UM01GznPziINTxib87tnEBFvRohuYB8q5rGesLotZd'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) #tenemos la autorización en auth

filename=open(argfile,'r')
f=filename.readlines()
filename.close()





if __name__ == '__main__':
    thread = stream.StreamThread(api,auth)
    thread.start()
    print("que pasa aqui")





"""if __name__ == '__main__':
    for tweet in tweepy.Cursor(api.user_timeline).items():
        if tweet.retweeted:
            print(tweet.text)"""
