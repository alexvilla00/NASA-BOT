import numpy as np
from DBinterface import nasaDBinterface

interface = nasaDBinterface()

if hashtag == 'ranking':
    ranking_size = 3 #pedir al usuario el numero de elementos
    top_or_bottom =  #pedir al usuario el numero de elemntos

    my_ranking = interface.getranking(ranking_size, bottom = False)

    api.update_status(status="@" + tweet.user.screen_name + print_ranking(my_ranking,ranking_size), in_reply_to_status_id=tweet.id )

def print_ranking(my_ranking,ranking_size):

    for i in range(ranking_size):
        print("1º ", my_ranking[i][0], "with a CO2 value of ", my_ranking[i][1])

    return()