#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
from config import create_api
import time
from functions import leer_hashtag

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read= open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write= open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        try:
            new_since_id = max(tweet.id, new_since_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            if any(keyword in tweet.text.lower() for keyword in keywords):
                TEXT = tweet.text
               
                try:
                    hashtag=leer_hashtag(TEXT)
                except Exception:
                    print("hashtag error")
                    hashtag=None

                logger.info(f"Answering to {tweet.user.name}")

                if hashtag=="consulta":
                    #v es un vector que guarda tanto las emision de CO2 como el puesto en el ranking
                    v=consulta()
                    api.update_status(status="@" + tweet.user.screen_name + "Your city is in the " + v[1] + 
                    " in the ranking. It emits " +v[0] "kg of CO2 per habitant.", in_reply_to_status_id=tweet.id )
                    print("mbn")

        except Exception:
            api.update_status(status="@" + tweet.user.screen_name + " This tweet has already been answered.", in_reply_to_status_id=tweet.id )
    return new_since_id

def main():
    hashtags=["#consulta"]
    api = create_api()
    since_id = read_last_seen(FILE_NAME)
    while True:
        since_id = check_mentions(api, hashtags, since_id)
        logger.info("Waiting...")
        store_last_seen(FILE_NAME, since_id)
        time.sleep(20)
    if

if __name__ == "__main__":
    main()