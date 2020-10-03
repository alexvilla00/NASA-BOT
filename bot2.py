import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("GkSKcH3MdcMEfsGxEUNWzuAXA")
    consumer_secret = os.getenv("DeuD2v9Zxg7teF3HknJUNaZSNmApk9vESEfJ5PP7DLlKwKirKG")
    access_token = os.getenv("1312298521161334784-XtkujR8oEpD0AwL0aUNl5ZyNYbCYtm")
    access_token_secret = os.getenv("JkMSJ5EFIwXqCBPydC7ObRJnyhdhdtD7BGJZqmXt9D1Vv")

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