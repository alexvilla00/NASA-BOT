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