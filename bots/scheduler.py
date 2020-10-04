import schedule
import time
import autoreply as ar
import config
import followfollowers as ff
import functions as fc

def autoreply(api):
    ar.main(api)

def followforfollow(api):
    ff.main(api)

def ranking(api):
    fc.rank(api)

schedule.every(5).minutes.do(autoreply)
schedule.every(10).minutes.do(followforfollow)
schedule.every().monday.at("15:00").do(ranking)

api=config.create_api
while True:
    schedule.run_pending()
    time.sleep(1)