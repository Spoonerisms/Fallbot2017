### imports required
import random
import tweepy


from pytz import timezone, utc

from time import sleep

from datetime import datetime, timedelta, date


"""
Commented out since I don't have this info
"""

from FallBotTwitterauth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


"""
setting this as the constant for TAPI
"""
TAPI = tweepy.API(auth)

### 
PHRASE_BOOK = [
    'Fall starts in %s',
    'Leaves start changing color in %s',
    'Time till fall: %s',
    "FML for the next %s",
    "No pumpin spice lattes for the next %s",
    "%s until I start my seasonal depression all over again",
    "My favorite season starts in %s",
]
FALL_START = datetime(2018, 9, 22)

LAST_RUN_LOG_FILE = 'last_run.log'


### Check if ran today - if false then maybe we should run
def ran_today():
    try:
        with open(LAST_RUN_LOG_FILE, 'r') as f:
            d = datetime.strptime(f.read(), "%Y-%M-%d").date()
            if datetime.now().date() == d:
                return True
            return False
    except IOError:
        print("File not found so running for first time.")
        return False

### logging if ran
def log_today():
    with open(LAST_RUN_LOG_FILE, 'w') as f:
        f.write(str(datetime.now().date()))

def get_time_till_fall():
    now = datetime.now()
    d = FALL_START - now

    # string formatting to make it look good
    d = str(d).split('.')[0] # remove miliseconds
    s = d.split(':')
    d = "%s hours, %s minutes and %s seconds" % (s[0], s[1], s[2])
    return d

def randomize_day():
    """
        I enjoyed this problem, how to randomize the post throughout the day.
        When the program runs - it takes the number of seconds that have passed today
        and a random number between 0 and total number of seconds in a day.
        If the random number is lower than the number of seconds passed in a day, then we posting for the day.
        We could normalize this but I like what we've got so far.

        Ex: Chance to run at midnight, very low, chance to run at noon 50%, chance to run at 11:59pm 100%.
    """

    seconds_in_day = 86400
    n = datetime.now()
    seconds_today = n.hour * 3600 + n.minute * 60 + n.second
    r = int(random.random() * 86400)
    if r < seconds_today:
        # sleep for a random 5 minutes to hide the fact it runs on 5 minute interval
        sleep(random.random() * 300)
        return True
    return False


def post_to_twitter():
    p = random.choice(PHRASE_BOOK) % get_time_till_fall()
    print(p)
    TAPI.update_status(p)

def run():
    if not ran_today() and randomize_day():
        post_to_twitter()
        log_today()


if __name__ == "__main__":
    """
    We assume crontab is run every 5 minutes
    """
    run()