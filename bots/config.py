import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    
    consumer_key = "7AWT4LssnLU2rhNKyB3sxwtRg"
    consumer_secret = "N1DrlHHOUo9MtF1ze0ysOY0KrwEobaNrYvaibmgmVIGWnzX4HV"
    access_token = "1311935958376423424-U3CNyyYObmocxrlZvsz584kxf8D5yW"
    access_token_secret = "v6XTptsEnrgghWvwq8DaXO84XIP3lS9gBs0Hd26uvXahF"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api