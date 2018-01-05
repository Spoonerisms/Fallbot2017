### imports required
import random
import tweepy


from pytz import timezone, utc

from time import sleep
from datetime import datetime, timedelta


### Commented out since I don't have this info

# from FallBotTwitterauth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


### setting this as the constant for TAPI
# TAPI = tweepy.API(auth)


PHRASE_BOOK = [
    'Fall starts in %s',
    'Leaves start changing color in %s',
    'Time till fall %s',
    "FML till %s",
]


FALL_START = datetime(2018, 9, 22)
LAST_RUN = datetime.today()

def get_time_till_fall():
    now = datetime.now()
    d = FALL_START - now

    time_map = {}
    d = str(d).split('.')[0]
    s = d.split(':')
    d = "%s hours, %s minutes and %s seconds" % (s[0], s[1], s[2])

    return d


def randomize_day():
    seconds_in_day = 86400
    time_to_run = int(random.random() * seconds_in_day)
    
    ### leave commented out until you know it works since this will halt the program for 0 - 24 hours
    # sleep(time_to_run)

def post_to_twitter():
    p = random.choice(PHRASE_BOOK) % get_time_till_fall()
    print p
    # TAPI.update_status(p)

def run():
    randomize_day()
    post_to_twitter()

if __name__ == "__main__":
    # We assume this function will run at midnight each day then randomly post during the day\
    run()