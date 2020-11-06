#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

if False:
    noppa_d100 =[i for i in range(1, 101)]
    print(noppa_d100)
    print(random.choice(noppa_d100))
    print(noppa_d100[random.randrange(100)])

def nopantahot(tahomaara=0):
    """ palauta tahomäärän mukaiset nopan silmäluvut listana """
    #print("nopantahot("+str(tahomaara)+")")
    lista=[]

    for target_list in range(tahomaara):
        lista.append(1+target_list)
    #print(lista)
    return lista

def noppa(tahomaara):
    """
    palauta satunnainen nopan silmäluku
    """
    #print("noppa("+str(tahomaara)+"):",end="")
    
    vastaus=1+random.randrange(tahomaara)
    #print(vastaus)
    return vastaus

def helppo(mode="print"):
    if mode=="print":
        print("""
        helppo:
        Kysy kauttajalta kuinka monta tahoista noppaa kayttaja haluaa heittaa.
        Tee funtio joka ottaa sisaansa tahojen lukumaaran ja palauttaa listan jossa on nopan silmaluvut.
        Anna satunnainen nopantulos printtaamalla se kayttajalle.
        """)
    tahot=int(input('Montako tahoa nopassa:'))
    #tahot=6
    tahot_lista=nopantahot(tahot)
    np=noppa(tahot)
    print ("lista silmäluvuista:"+str(tahot_lista))
    print ("nopan tulos:"+str(np))


#def helppo(mode) ends

def normaali(mode="print"):
    if mode=="print":
        print ("""
        normaali
        sama kuin normaali, mutta kysy kuinka monta noppaa kayttaja haluaa heittaa, ja printtaa
        noppien tulos erikseen ja summana
        """)
    lista=[]
    nopatlkm=int(input('Montako noppaa:'))
    tahot=int(input('Montako tahoa nopassa:'))
    #tahot=100
    #nopatlkm=15
    summa=0

    for i in range(nopatlkm):
        lista.append(noppa(tahot))
        summa+=lista[i]

    print("summa:"+str(summa)+", silmäluvut: ",end="")
    print (lista)
#def normaali(mode) ends

def vaikea(mode="print"):
    if mode=="print":
        print ("""
        #vaikea
        Sama kuin normaali, mutta tuloksen jalkeen kysy kayttajalta halutaanko heittaa uudelleen.
        entterilla uusi heitto
        muuta noppa kysyy uudelleen tahot
        muuta noppien lukumaara kysyy noppaluvun uudelleen
        lopeta lopettaa ohjelman
        """)
#def vaikea(mode) ends

if __name__ == "__main__":
#    helppo("noprint")
   normaali("noprint")
#   vaikea("noprint")
