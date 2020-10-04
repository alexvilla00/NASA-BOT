import schedule
import time
import autoreply as ar
import config
import followfollowers as ff
import functions as fc
import concienciar

class Count(object):

    def __init__(self):
        self._count = 1

    def increase(self):
        self._count += 1


def autoreply(api):
    ar.main(api)

def followforfollow(api):
    ff.main(api)

def ranking(api):
    fc.rank(api)

def mensajes(api, vector, count):
    concienciar(api, vector, count)
    count.increase()
    if count._count==24:
        count.__init__()


f = open("mss.txt", 'r')
vector=[""]
i=0
for line in f:
    vector.append(line)
    i+=1
f.close()
vector.pop(0)

schedule.every(5).minutes.do(autoreply)
schedule.every(10).minutes.do(followforfollow)
schedule.every().monday.at("15:00").do(ranking)
schedule.every().day.at("15:00").do(mensajes, vector, count)

api=config.create_api
vector
while True:
    schedule.run_pending()
    time.sleep(1)


