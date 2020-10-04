from DBinterface import nasaDBinterface  
import random 
import datetime as dt

def print_ranking(my_ranking,ranking_size,top_or_bottom):
    Tweet=""
    if top_or_bottom == True:
        Tweet += ("The first " + ranking_size + " cities with more CO2 emissions due to traffic are: \r\n ")     
    else: 
        Tweet += ("The first " + ranking_size + " cities with less CO2 emissions due to traffic are: \r\n" +
        "Congratulations!!!!! The Earth loves you :D \r\n")  

    for i in range(ranking_size):
        Tweet += (str((i+1)) + "º " + str(my_ranking[i][0]) + " with a CO2 value of " + str(my_ranking[i][1]) + "\r\n")
    return(Tweet)

def rank(api):

    d=dt.datetime.today().weekday()
    h=dt.datetime.today().hour()
    m=dt.datetime.today().minute()
    if d==0 and h==14 and m==0:
        interface = nasaDBinterface()
        ranking_size = random.randint(2,10)
        top_or_bottom =  random.choice([True, False]) 
        my_ranking = interface.getranking(ranking_size, top_or_bottom)
        Tweet=print_ranking(my_ranking,ranking_size,top_or_bottom)

        api.update_status(status=Tweet)
  

def leer_hashtag(T):

    L=list(T)
    L.append(" ")
    for a in range(len(L)):
        if L[a]=="#":
            a=a+1
            ht=[]
            while L[a]!=" ":
                ht.append(L[a])
                a=a+1
    ht_salida= ""
    for e in ht:
        ht_salida += e
    return ht_salida
