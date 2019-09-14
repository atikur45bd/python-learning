import tweepy
import time
from credentials import*

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


fh = open('1984.txt')
contents = fh.read()
fh.close()

len_of_content = len(contents)
first = 0
last = 160

while len_of_content != 0:
    t = contents[first: last].replace('\n', ' ')
    api.update_status(t)
    first += last
    last += last
    len_of_content -= last
    time.sleep(120)
