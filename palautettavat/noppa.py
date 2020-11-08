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
    #print ("lista silmäluvuista:"+str(tahot_lista))
    #kommentoitu, koska ei pyydetty tulostamaan
    print ("nopan tulos:"+str(np))
#def helppo(mode) ends

def normaali(mode="print"):
    if mode=="print":
        print ("""
        normaali
        sama kuin normaali, mutta kysy kuinka monta noppaa kayttaja haluaa heittaa, ja printtaa
        noppien tulos erikseen ja summana
        """)
    
    nopatlkm=int(input('Montako noppaa:'))
    #nopatlkm=15
    tahot=int(input('Montako tahoa nopassa:'))
    #tahot=100

    lista=[]
    summa=0

    for i in range(nopatlkm):
        lista.append(noppa(tahot))
        summa+=lista[i]

    print("summa:"+str(summa)+", silmäluvut: ",end="")
    print (lista)
#def normaali(mode) ends

class noppaluokka(object):
    """
    luokka mallintaa rajatun sivumäärän nopan
    """
    def __init__(self,tahot):
        """
        constructor
        """
        #print("noppaluokka::__init__(",end="")
        self.tahot = tahot
        self.arvo=1+random.randrange(tahot)
        #print(str(tahot)+")")

    def pudota(self):
        """
        pudota ja näytä silmäluku
        """
        self.arvo = 1+random.randrange(self.tahot)
        #print("pudota:"+str(self.arvo))

    def __del__(self):
        """
        destructor
        """
        #print("noppaluokka::__del__ noppa oli:"+str(self.arvo)+"/"+str(self.tahot))

    def katso(self):
        """
        tulosta nopan arvo
        """
        print("katso: "+str(self.arvo))
        return self.arvo

    pass
#class noppaluokka(object)

class noppalistaluokka(object):
    """
    lista useasta nopasta
    """
    def __init__(self):
        """
        create and zero
        """
        self.count=0
        self.noppalista=[]

    def sido(self,noppa):
        """
        append list
        """
        self.noppalista.append(noppa)
        self.count+=1
        #print(self.count)

    def vapauta(self,noppaindex):
        """
        free certain noppa from list
        """
        print("vapauta("+str(noppaindex+1)+"/"+str(self.count)+")")
        poisnoppa = self.noppalista.pop(noppaindex)
        self.count-=1

        #huom: noppa tuhoutuu kun ei enää käytössä.
        return poisnoppa

    def show(self,num):
        """
        show
        """
        return self.noppalista[num]
    pass
#class noppalistaluokka(object) ends


def vaikea(mode="print"):
    if mode=="print":
        print(
"""
#vaikea
Sama kuin normaali, mutta tuloksen jalkeen kysy kayttajalta halutaanko heittaa uudelleen.
entterilla uusi heitto
muuta noppa kysyy uudelleen tahot
muuta noppien lukumaara kysyy noppaluvun uudelleen
lopeta lopettaa ohjelman
""")

    #nopatlkm=int(input('Montako noppaa:'))
    nopatlkm=5
    #tahot=int(input('Montako tahoa nopassa:'))
    tahot=100

    noppalistaolio = noppalistaluokka()

    #testcase luo alkuun yksi noppa
    #noppalistaolio.sido(noppaluokka(2))

    for var in range(nopatlkm):
        noppalistaolio.sido(noppaluokka(tahot))

    #testcase luo loppuun yksi noppa
    #noppalistaolio.sido(noppaluokka(4))

    #testcase luo tulosta tulokset
    for var in range(noppalistaolio.count):
        noppalistaolio.show(var).katso()

    kysymys= input("operaatio(muuta noppa/muuta lukumäärä/lopeta")
    #print("noppalista sisältää "+str(noppalistaolio.count)+" noppaa")
    #for var in range(noppalistaolio.count):
    #    noppalistaolio.vapauta(0)
    #    #vapauta aina ensimmäinen noppa, koska vapautus pienentää listaa yhdellä

    #print("tuhoutuu:")
    #noppalistaolio.vapauta(3)
    #print("ei tuhoutuu:")
    #np=noppalistaolio.vapauta(2)
    #print("done")
    
    #print("tuhotaan:");    np="";    print("tuhoutui:")
    #print("noppalista sisältää "+str(noppalistaolio.count)+" noppaa")

"""
    for target_list in noppalista:
        print("list:"+str(target_list.arvo))
        pass

    print ("noppaluokka: "+str(noppaolio.katso()))
"""
#def vaikea(mode) ends

if __name__ == "__main__":
    print ("")
    print ("")
    #helppo("noprint")
    #normaali("noprint")
    vaikea("print")
