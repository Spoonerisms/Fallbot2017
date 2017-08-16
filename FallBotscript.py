import tweepy
from FallBotTwitterauth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import time

ts = time.time()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def countdown(n) :
while n > 0:
print (n)
n = n - 1
if n ==0:
print('There are (n) days until fall.')
#countdown(50)