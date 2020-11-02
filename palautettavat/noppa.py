#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

noppa_d100 =[i for i in range(1, 101)]
print(noppa_d100)

print(random.choice(noppa_d100))
print(noppa_d100[random.randrange(100)])

#helppo
#Kysy kauttajalta kuinka monta tahoista noppaa kayttaja haluaa heittaa.
#Tee funtio joka ottaa sisaansa tahojen lukumaaran ja palauttaa listan jossa on nopan silmaluvut.
#Anna satunnainen nopantulos printtaamalla se kayttajalle.

#normaali
#sama kuin normaali, mutta kysy kuinka monta noppaa kayttaja haluaa heittaa, ja printtaa
# noppien tulos erikseen ja summana

#vaikea
#Sama kuin normaali, mutta tuloksen jalkeen kysy kayttajalta halutaanko heittaa uudelleen.
#entterilla uusi heitto
#muuta noppa kysyy uudelleen tahot
#muuta noppien lukumaara kysyy noppaluvun uudelleen
#lopeta lopettaa ohjelman